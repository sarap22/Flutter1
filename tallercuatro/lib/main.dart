import 'package:flutter/material.dart';
void main() {
  runApp(const MyApp());
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a blue toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      body:
      Column(
          children:[
            Container(
              width: double.infinity,
              height:500,
              padding:const EdgeInsets.only(left: 15, right: 15, top: 30, bottom: 10),
              color: Colors.grey,
              margin: const EdgeInsets.only(left: 15, right: 15, top: 60, bottom: 10),
              child:Column(
                  children:[
                    Text(
                      "Native Application", textAlign:  TextAlign.center,
                      style: TextStyle(color: Colors.white,
                          fontSize: 30),
                    ),
                    Container(
                      width: double.infinity,
                      height: 300,
                      margin: const EdgeInsets.only(left: 15, right: 15, top: 60),
                      child: Image.network("https://i.pinimg.com/originals/94/83/ba/9483ba3eae0011a9909f52a0e69a85ce.png"),
                    )]
              ),
            ),
            Container(
              width: double.infinity,
              height: 130,
              color: Colors.orange,
              margin: const EdgeInsets.only(left: 15, right: 15, top: 80),
              child: Container(
                padding:const EdgeInsets.only(left: 15, right: 15, top: 30, bottom: 10),
                child: Text(
                  "Device APIS", textAlign:  TextAlign.center,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(fontSize: 50, color: Colors.white),
                ),
              ),
            )]
      ),
      // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
