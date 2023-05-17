<template>
  <mu-list>
    <mu-list-item button :ripple="false" @click="fingerprintVerification">
      <mu-list-item-title> 指纹验证 </mu-list-item-title>
      <mu-list-item-action>
        <mu-switch v-model="zhiwen" readonly></mu-switch>
      </mu-list-item-action>
    </mu-list-item>
  </mu-list>
  //组件
  <finger-print v-if="showFinger" :fingertext="fingertext" @cancel="cancel_from"></finger-print>
</template>



<script>
import FingerPrint from '@/components/Fingerprint'

component={
	'finger-print': FingerPrint
}
data() ({
	return :{
		zhiwen: false,
		showFinger: false,
		fingertext: '请扫描指纹'
	}
})
//开启指纹验证
fingerprintVerification() {
	let _this = this;
	if (this.zhiwen) {
		this.zhiwen = false;
		return;
	}
	if (!window.plus) return;
	// 检查是否支持指纹识别
	if (plus.fingerprint) {
		if (!plus.fingerprint.isSupport()) {
			plus.nativeUI.alert('此设备不支持指纹识别');
			return;
		}
		if (!plus.fingerprint.isKeyguardSecure()) {
			plus.nativeUI.alert('此设备未设置密码锁屏，无法使用指纹识别');
			return;
		}
		if (!plus.fingerprint.isEnrolledFingerprints()) {
			plus.nativeUI.alert('此设备未录入指纹，请到设置中开启');
			return;
		}

		//开启指纹识别验证()
		this.showFinger = true
		this.fingertext = '请扫描指纹'

		var waiting = null;
		plus.fingerprint.authenticate(function () {
			plus.nativeUI.alert('指纹识别成功');
			_this.zhiwen = true
			_this.showFinger = false;
		}, function (e) {
			switch (e.code) {
				case e.AUTHENTICATE_MISMATCH:
					plus.nativeUI.toast('指纹匹配失败，请重新输入');
					_this.fingertext = '指纹匹配失败，请重试'
					break;
				case e.AUTHENTICATE_OVERLIMIT:
					plus.nativeUI.alert('指纹识别失败次数超出限制，请使用其它方式进行认证');
					_this.showFinger = false;
					break;
				default:
					plus.nativeUI.alert('指纹识别失败(' + e.code + ')，请重试');
					_this.fingertext = '指纹识别失败(' + e.code + ')，请重试'
					break;
			}
		})

	} else {
		plus.nativeUI.alert('当前环境不支持指纹识别API，请更新到最新版本');
	}
}
</script>