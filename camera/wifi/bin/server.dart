import 'dart:convert';
import 'dart:io';

import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart';
import 'package:shelf_router/shelf_router.dart';

final _router = Router()
  ..get('/', _rootHandler)
  ..get('/wifi', _wifiHandler);

Response _rootHandler(Request req) {
  return Response.ok('Hello, World!\n');
}

Future<Response> _wifiHandler(Request request) async {
  final File input = File('/signal');
  final List<String> lines = await input.readAsLines();
  if(lines.length != 3) Response.internalServerError(body: 'Wrong format for Wifi signal file');
  final List<String> data = lines[2].split(RegExp('\\s+'));
  final String signal = data[4].replaceAll('.', '');
  return Response.ok(jsonEncode({
    'status' : int.tryParse(signal) ?? 0
  }));
}

void main(List<String> args) async {
  final handler = Pipeline().addMiddleware(logRequests()).addHandler(_router);
  final port = int.parse(Platform.environment['PORT'] ?? '8080');
  final server = await serve(handler, InternetAddress.anyIPv4, port);
  print('Server listening on port ${server.port}');
}