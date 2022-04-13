<script>
	import reglWrapper from 'regl';
	import createCamera from 'regl-camera';
	import reglLines from 'regl-gpu-lines';
	import { min, max } from 'd3-array';
	import glmat4 from 'gl-mat4';

	import { getContext } from 'svelte';
	import { cubicInOut } from 'svelte/easing';

	const { data, width, height, custom, xGet, yGet } = getContext('LayerCake');
	const { speedFactor, play, next, prev, rewind } = getContext('MediaControls');
	const { gl } = getContext('gl');

	let regl;

	const trailLength = $data.findIndex((d) => d.fullYear == 1890); // ten years trail
	const pause = 0.5 * trailLength;
	const points = $data.map((d, idx) => [idx, $yGet(d), $xGet(d), d.diffTemp]);
	const numPoints = points.length;
	const maxAbsDiff = max($data, (d) => Math.abs(d.diffTemp));

	const vertShader = `
		#define PI 3.1415926538

		precision highp float;

		uniform mat4 projection, rotateZ, view;
    uniform float width, currentIndex, maxAbsDiff, numPoints, trailLength;

    #pragma lines: attribute vec4 data;
		#pragma lines: position = getPosition(data);
		#pragma lines: width = getWidth();
		#pragma lines: varying vec4 color = getColor(data);

    vec4 getPosition(vec4 data) {
			float index = data.x;
			float theta = data.y - PI / 2.0;
			float radius = data.z;
			float pause = 0.5 * trailLength;

			float x = radius * cos(theta);
			float y = -radius * sin(theta);
			float z = (2.0 * index / numPoints - 1.0);
			float zScale = 0.01;

			if (currentIndex > numPoints + pause) {
				float slope = (currentIndex - numPoints - pause) / trailLength;
				zScale = 0.74 * smoothstep(0.0, 1.0, slope / 2.0) + 0.01;
			}

			z = zScale * z;
      return projection * view * rotateZ * vec4(x, y, z, 1);
    }

		float getWidth() {
			return width;
		}

		vec4 getColor(vec4 data) {
			float index = data.x;
			float diff = data.w;
			float opacity = 1.0;
			float pause = 0.5 * trailLength;

			if (currentIndex <= numPoints + pause) {
				float border = min(currentIndex, numPoints);
				// opacity = sqrt(smoothstep(border - trailLength, border, index)); // short trail
				opacity = pow(smoothstep(border - trailLength, border, index), 0.2); // medium trail
				// opacity = step(border - trailLength, index); // long trail
				if (index > currentIndex) opacity = 0.0;
			}

			if (currentIndex > numPoints + pause) {
				float x = numPoints - trailLength;
				float threshold = x * (1.0 - smoothstep(numPoints + pause, numPoints + pause + 2.0 * trailLength, currentIndex));
				opacity = min(pow(smoothstep(0.0, maxAbsDiff, abs(diff)), 0.1), step(threshold, index));
			};

			vec3 redColor = vec3(0.404, 0.0, 0.122);
			vec3 blueColor = vec3(0.019, 0.188, 0.38);
			vec3 zeroColor = vec3(1.0, 1.0, 1.0);

			float diffNorm = 2.0 * smoothstep(-maxAbsDiff, maxAbsDiff, diff) - 1.0;

			if (diffNorm < 0.0) {
				return vec4(mix(zeroColor, blueColor, -diffNorm), opacity);
			} else {
				return vec4(mix(zeroColor, redColor, diffNorm), opacity);
			}
    }`;

	const fragShader = `
    precision highp float;
		varying vec4 color;

		void main () {
      gl_FragColor = color;
    }`;

	function resize() {
		if ($gl) {
			const canvas = $gl.canvas;

			const dpr = window.devicePixelRatio;
			const displayWidth = Math.round(canvas.clientWidth * dpr);
			const displayHeight = Math.round(canvas.clientHeight * dpr);

			if (canvas.width !== displayWidth || canvas.height !== displayHeight) {
				canvas.width = displayWidth;
				canvas.height = displayHeight;
			}

			$gl.viewport(0, 0, canvas.width, canvas.height);
		}
	}

	function render() {
		if ($gl) {
			regl = reglWrapper({
				gl: $gl,
				pixelRatio: window.devicePixelRatio,
				extensions: ['ANGLE_instanced_arrays']
			});

			const camera = createCamera(regl, {
				theta: Math.PI / 2,
				center: [0, 0, 0],
				damping: 0,
				noScroll: true,
				renderOnDirty: true,
				mouse: false
			});

			const drawLines = reglLines(regl, {
				vert: vertShader,
				frag: fragShader,
				uniforms: {
					width: (ctx, props) => ctx.pixelRatio * props.width,
					projection: () => {
						return glmat4.ortho([], -1.0, 1.0, -1.0, 1.0, 0.01, 100.0);
					},
					rotateZ: regl.prop('rotateZ'),
					currentIndex: regl.prop('currentIndex'),
					maxAbsDiff: regl.prop('maxAbsDiff'),
					numPoints: regl.prop('numPoints'),
					trailLength: regl.prop('trailLength')
				},
				depth: { enable: true },
				blend: {
					enable: true,
					func: {
						srcRGB: 'src alpha',
						srcAlpha: 'src alpha',
						dstRGB: 'one minus src alpha',
						dstAlpha: 'one minus src alpha'
					}
				}
			});

			const lineData = {
				width: 3,
				join: 'round',
				cap: 'round',
				joinResolution: 1,
				vertexCount: points.length,
				vertexAttributes: { data: regl.buffer(points) }
			};

			const index2000 = $data.findIndex((d) => d.fullYear == 2000);

			regl.frame(async () => {
				if ($rewind) $custom.currentIndex -= $speedFactor * 100;

				if ($custom.currentIndex < 0) {
					$rewind = false;
					$play = false;
					$custom.currentIndex = 0;
				}

				if ($next) {
					$custom.currentIndex += ($speedFactor * trailLength) / 10 / 12;
					$play = false;
					$rewind = false;
					$prev = false;
					$next = false;
				}

				if ($prev) {
					$custom.currentIndex = Math.max(
						$custom.currentIndex - ($speedFactor * trailLength) / 10 / 12,
						0
					);

					$play = false;
					$rewind = false;
					$prev = false;
					$next = false;
				}

				if ($play) {
					if ($custom.currentIndex >= index2000)
						$custom.currentIndex += $speedFactor * 5;
					else $custom.currentIndex += $speedFactor * 20;
				}

				let angle = 0;
				if ($custom.currentIndex > numPoints + pause - 1) {
					let theta = Math.PI;
					const slope = ($custom.currentIndex - numPoints - pause + 1) / 2400;
					const rotate = min([slope, 1.0]);
					theta = ((1 + cubicInOut(rotate)) * Math.PI) / 2;
					angle = 2 * slope * Math.PI;
					camera.update({ theta });
				}

				camera.dirty = true;

				camera(() => {
					regl.clear({ color: $gl.COLOR_BUFFER_BIT });

					drawLines([
						{
							...lineData,
							currentIndex: $custom.currentIndex,
							maxAbsDiff,
							numPoints,
							trailLength,
							rotateZ: glmat4.rotateZ([], glmat4.create(), angle)
						}
					]);
				});
			});
		}
	}

	$: $width, $height, $gl, resize(), render();

	$: setTimeout(() => ($play = true), 1200);
</script>
