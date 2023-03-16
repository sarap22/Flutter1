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

  get width => null;

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
        children: [
          Container(
            width:double.infinity,
            height:100,
            color: Colors.grey[800],
            margin: const EdgeInsets.only(left: 5, right: 5, top: 20, bottom: 10),
            padding:const EdgeInsets.only(top: 20, bottom: 10),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.only(left: 10, right: 10),
                  child: SizedBox(
                    width:30,
                  height:50,
                  child:
                  Image.network("https://cdn-icons-png.flaticon.com/512/8390/8390843.png"),
                  ),
                ),Column(
                  children:[
                Container(
                  margin: const EdgeInsets.only(top:15,right: 10,bottom: 10),
                  child: Text(
                    "LECCIONES DESTACADAS", textAlign:  TextAlign.center,
                    style: TextStyle(color: Colors.white,
                        fontSize: 20),
                  ),
                ), Text(
                      "Eva Samper", textAlign:  TextAlign.center,
                      style: TextStyle(color: Colors.white,
                          fontSize: 10),
                    )
                ]),
            Container(
              margin: const EdgeInsets.only(right: 10, bottom: 10),
              child: SizedBox(
                width:30,
                height:50,
                child:
                Image.network("https://cdn-icons-png.flaticon.com/512/2311/2311526.png"),
              ),
            ),
                Container(
                  margin: const EdgeInsets.only(right: 2),
                  child: SizedBox(
                    width:30,
                    height:50,
                    child:
                    Image.network("https://cdn-icons-png.flaticon.com/512/1177/1177568.png"),
                  ),
                ),],
            ),
          ),
          Column(
              children: [
                Container(
                  color: Colors.green,
                  width:double.infinity,
                  height: 200,
                  margin: const EdgeInsets.only(left: 15, right: 15, top: 7, bottom: 10),
                  child:
                  Image(
                    image: NetworkImage('https://cdn-icons-png.flaticon.com/512/3614/3614152.png'),
                  ),
                ),
                Container(
                  margin: const EdgeInsets.only(left: 5, right: 5, top: 10, bottom: 10),
                  child: Column(
                  children: [
                  Text(
                  "METRICAS", textAlign:  TextAlign.center,
                  style: TextStyle(color: Colors.green,
                      fontSize: 20),
                  ),
                    Text(
                      "ENCUENTRA A TU CLIENTE IDEAL ANALIZANDO LOS CICLOS DE VIDA", textAlign:  TextAlign.center,
                      style: TextStyle(color: Colors.black,
                          fontSize: 30),
                    ),
                    Container(
                      margin: const EdgeInsets.only(left: 35, right: 15, top: 20, bottom: 10),
                      child:
                      Row(
                        children: [
                          Image(
                            image: NetworkImage('https://cdn-icons-png.flaticon.com/512/639/639434.png'),
                            width: 20,
                            height: 20,
                          ),
                          Container(
                            child: Text(
                              "5 min -", textAlign:  TextAlign.center,
                              style: TextStyle(color: Colors.black,
                                  fontSize: 20),
                            ),
                          ),
                          Text(
                            " Por el equipo del poder", textAlign:  TextAlign.center,
                            style: TextStyle(color: Colors.black,
                                fontSize: 20),
                          ),
                        ],
                      ),
                    ),
                    Container(
                      padding:const EdgeInsets.only(top: 20, bottom: 20,left:15),
                      color: Colors.grey.shade200,
                      child: Column(
                        children: [
                          Row(
                            children: [
                              Image(
                                image: NetworkImage('https://cdn-icons-png.flaticon.com/512/7457/7457418.png'),
                                width: 50,
                                height:50,
                              ),
                              Text(
                                " Plantillas bloqueadas", textAlign:  TextAlign.center,
                                style: TextStyle(color: Colors.black,
                                    fontSize: 20),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                    Container(
                      color: Colors.green.shade600,
                      width:double.infinity,
                      height: 80,
                      margin: const EdgeInsets.only(left: 5, right: 5, top: 10),
                      child:
                      Image(
                        image: NetworkImage('https://cdn-icons-png.flaticon.com/512/1080/1080436.png'),
                        width: 20,
                        height: 20,
                      ),
                    )
                  ],
                ),
                )
              ],
          ),
        ],
      ),
    );
  }
}
