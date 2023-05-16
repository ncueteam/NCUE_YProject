//import 'dart:js_util';
//import 'dart:async';
//import 'dart:html';

import 'dart:html';

import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:flutter_webview_plugin/flutter_webview_plugin.dart';

void main() {
  runApp(
    MaterialApp(
      theme: ThemeData(useMaterial3: true),
      home: const WebViewApp(),
    ),
  );
}

class WebViewApp extends StatefulWidget {
  const WebViewApp({super.key});

  @override
  State<WebViewApp> createState() => _WebViewAppState();
}

class _WebViewAppState extends State<WebViewApp> {
  late final WebViewController controller;

  final _resultInfo = 'Hello,Vue!';
  final flutterWebViewPlugin = FlutterWebviewPlugin();

  /*if (Platform.isAndroid) {
      WebView.platform = SurfaceAndroidWebView();
    }*/
  /*public void setAllowFileAccess(bool allow){
    setAllowFileAccess(true);
  }

  void setAllowFileAccessFromFileURLs(bool allow) {
    setAllowFileAccessFromFileURLs(true);
  }*/

  /*void initWebViewSettings(final context) {
    WebSettings webSetting = this.getSettings();
    webSetting.setAllowFileAccess(true);
    webSetting.setAllowFileAccessFromFileURLs(true);
  }*/

  @override
  void initState() {
    super.initState();
    controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..loadRequest(
        Uri.parse('assets/vue-soft-ui-dashboard-main/src/views/Profile.vue'),
        //'assets/Profile.vue'
      )
      ..addJavaScriptChannel('getInfoFromVue',
          onMessageReceived: (JavaScriptMessage message) {
        debugPrint('收到消息${message.message}');
        flutterWebViewPlugin
            .evalJavascript("window.getInfoFromFlutter('$_resultInfo')")
            .then((result) {})
            .catchError((onError) {});
      });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter WebView'),
      ),
      body: WebViewWidget(
        controller: controller,
      ),
    );
  }

  /*void setallowfileaccess(bool allow) {
    //setAllowFileAccess(true);
  }

  void setallowfileaccessfromfileURLs(bool allow) {
    setAllowFileAccessFromFileURLs(true);
  }*/
  /*void _updateSettings() async {
    if (controller != null) {
      await controller!.evalJavascript(
        // Modify the WebView settings
        if (window.androidBridge) {
          // Check if the Android WebView bridge object exists (for Android)
          window.androidBridge.setAllowFileAccess($allow);
        } else {
          // Otherwise, use default settings
          console.warn('WebView bridge object not found.');
        }
      );
    }
  }*/

  @override
  void dispose() {
    flutterWebViewPlugin.dispose();
    super.dispose();
  }
}
