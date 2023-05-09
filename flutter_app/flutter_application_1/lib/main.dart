//import 'dart:js_util';
//import 'dart:async';
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

  void setAllowFileAccess(bool allow) {
    //allow = true;
    setAllowFileAccess(true);
  }

  void setAllowFileAccessFromFileURLs(bool allow) {
    //allow = true;
    setAllowFileAccessFromFileURLs(true);
  }

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
        Uri.parse('file:///C:/Users/HP/Desktop/vue-soft-ui-dashboard-main/src/views/Profile.vue'),
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

  @override
  void dispose() {
    flutterWebViewPlugin.dispose();
    super.dispose();
  }
}

/*javascriptChannels: <JavascriptChannel>[
        JavascriptChannel(
            name: 'getInfoFromVue',
            onMessageReceived: (JavascriptMessage message) {
              print("收到的参数传入：" + message.message); //String Hello,Flutter
              //通过evalJavascript()方法调用vue挂载到window的方法
              flutterWebViewPlugin
                  .evalJavascript("window.getInfoFromFlutter('$_resultInfo')")
                  .then((result) {})
                  .catchError((onError) {});
              }),
        ].toSet(),*/
/*_webController?.evaluateJavascript('callJS("visible")')?.then((result) {
// You can handle JS result here.lt here.

});*/
/*void main() => runApp(WebViewStack());

class WebViewStack extends StatefulWidget {
  const WebViewStack({super.key});

  @override
  State<WebViewStack> createState() => _WebViewStackState();
}

class _WebViewStackState extends State<WebViewStack> {
  var loadingPercentage = 0;
  late final WebViewController controller;

  @override
  void initState() {
    super.initState();
    controller = WebViewController()
      ..setNavigationDelegate(NavigationDelegate(
        onPageStarted: (url) {
          setState(() {
            loadingPercentage = 0;
          });
        },
        onProgress: (progress) {
          setState(() {
            loadingPercentage = progress;
          });
        },
        onPageFinished: (url) {
          setState(() {
            loadingPercentage = 100;
          });
        },
      ))
      ..loadRequest(
        Uri.parse(
            'https://demos.creative-tim.com/vue-soft-ui-dashboard/?_ga=2.40006242.1313587345.1677913035-1103293509.1665758636#/profile'),
      );
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        WebViewWidget(
          controller: controller,
        ),
        if (loadingPercentage < 100)
          LinearProgressIndicator(
            value: loadingPercentage / 100.0,
          ),
      ],
    );
  }
}*/

/*
void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
          child: Text('Hello World!'),
        ),
      ),
    );
  }
}*/

/*class Webview extends StatefulWidget {
  @override
  WebViewState createState() => WebViewState();
}

class WebViewState extends State<Webview> {

  var _resultInfo = 'Hello,Vue!';
  FlutterWebviewPlugin flutterWebViewPlugin = new FlutterWebviewPlugin();

  @override
  Widget build(BuildContext context) {
    return WebviewScaffold(
      //要打开的网址,此处以百度为例
      url: 'https://demos.creative-tim.com/vue-soft-ui-dashboard/?_ga=2.40006242.1313587345.1677913035-1103293509.1665758636#/profile',
      javascriptChannels: <JavascriptChannel>[
        JavascriptChannel(
            name: 'getInfoFromVue',
            onMessageReceived: (JavascriptMessage message) {
              print("收到的参数传入：" + message.message); //String Hello,Flutter
              //通过evalJavascript()方法调用vue挂载到window的方法
              flutterWebViewPlugin
                  .evalJavascript("window.getInfoFromFlutter('$_resultInfo')")
                  .then((result) {})
                  .catchError((onError) {});
            }),
      ].toSet(),
    );
  }
}*/

/*final Completer<WebViewController> _webController = Completer<WebViewController>();

@override
Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: <Widget>[
            WebView(
                // h5页面的地址
                initialUrl: 'https://test.com/article-detail.html',
                // JS执行模式, 允许JS执行
                javascriptMode: JavascriptMode.unrestricted,
                // hh5可以根据navigator.userAgent判断当前环境
                userAgent: 'FlutterApp',
                // 在WebView创建完成后调用，只会被调用一次
                onWebViewCreated: (WebViewController webController) { 
                    // 获取到WebViewController实例
                    _webController.complete(webController);
                },
        
                // WebView加载完毕时的回调
                onPageFinished: (String url) {
                    // flutter调用js
                    _webController.future.then((controller){
                        var name = 'test'; // 方法名
                        var data = 'hello'; // 传递的参数
                        controller.evaluateJavascript("$name('$data')");
                    });
                },
                  
                // js调用flutter
                javascriptChannels: <JavascriptChannel>[
                    JavascriptChannel(
                        name: 'hide_loading', // 需要与h5一致
                        onMessageReceived: (JavascriptMessage msg) {
                            // print("参数： ${msg.message}");
                            // 关闭骨架屏加载效果
                            setState(() {
                                loading = false;
                            });
                        }
                    ),
                ].toSet(),
            ),
                
            // 骨架屏加载
            Visibility(
              visible: loading,
              child: SkeletonPage()
            )
        ]
      );
    );
}*/

/*class WebViewWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Webview example'),
      ),
      body: WebViewController(
        initialUrl:
            'https://demos.creative-tim.com/vue-soft-ui-dashboard/?_ga=2.40006242.1313587345.1677913035-1103293509.1665758636#/profile',
        javascriptMode: JavascriptMode.unrestricted,
      ),
    );
  }
}*/

/*class WebViewState extends State<Webview> {

  var _resultInfo = 'Hello,Vue!';
  FlutterWebviewPlugin flutterWebViewPlugin = new FlutterWebviewPlugin();

  @override
  
}*/