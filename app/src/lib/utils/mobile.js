import MobileDetect from 'mobile-detect';

export const isPhone = () => {
	const mobileDetect = new MobileDetect(navigator.userAgent);

	return mobileDetect.phone();
};
