<template>
	<div class="finger-print">
		<!--弹窗-->
		<div class="white_content">
			<div style="height: 220px;text-align: center;">
				<div style="padding:20px">
					<i class="iconfont" style="font-size: 50px;color: #B9862F;">&#xe72f;</i>
					<p style="font-size: 16px;color: black;">{{fingertext ||'请扫描指纹'}}</p>
					<p style="font-size: 12px;color: black;">验证身份以完成交易</p>
				</div>
			</div>
			<div class="btn">
				<div class="btn-cancel" @click="cancel()">取消</div>
			</div>
		</div>
		<!--覆盖层-->
		<div class="black_overlay"></div>
	</div>
</template>
 
<script>
	export default {
		name: 'smsCode',
		data() {
			return {
				
			}
		},
		mounted() {
			
		},
		methods: {
			//取消
			cancel(){
				this.$emit('cancel');
			}
		},
		
		props: {
			fingertext: {
				type: String,
				require: true,
			},
		},
		computed: {
			
		},
		watch: {
			
		}
	}
</script>
 
<style scoped>
	.finger-print {
		
	}
/**
弹窗样式
**/
	.finger-print .white_content {
		position: fixed;
		top: 50%;
		left: 50%;
		width: 80%;
		min-height: 220px;
		border: 1px solid #D6E9F1;
		border-radius: 8px;
		background-color: white;
		z-index: 99999999;
		transform: translate(-50%, -50%);
	}
 
	.finger-print .btn {
		height: 50px;
		line-height: 50px;
		position: absolute;
		bottom: 0;
		width: 100%;
		border-top: 1px solid #f5f5f5;
	}
	
	.finger-print .btn .btn-cancel {
		color: #B9862F;
		float: left;
		font-size: 14px;
		width: 100%;
		background-color: white;
		border-bottom-left-radius: 8px;
		border-right: 1px solid #f5f5f5;
		text-align: center;
	}
	/**
 * 覆盖层样式
 */
	.finger-print .black_overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, .6);
		z-index: 99999998;
		opacity: .80;
	}
</style>