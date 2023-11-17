    # pip install spyne
    from spyne import Application, ServiceBase, Unicode, rpc
    from spyne.protocol.soap import Soap11
    from spyne.server.wsgi import WsgiApplication

    class D3_BB13(ServiceBase):
        @rpc(Unicode, _returns=Unicode)
        def ola(ctx, name):
            return "Ola, {}".format(name)

        @rpc(_returns=Unicode)
        def ping(ctx):
            return "ping"

        @rpc(Unicode, Unicode, _returns=Unicode)
        def concat(ctx, a, b):
            return a + b

        @rpc(Unicode, _returns=Unicode)
        def contagem_regressiva(ctx, n):
            n = int(n)
            s = ""
            for i in range(n):
                s += f"{n-i}\n"
            return s

    application = Application([D3_BB13], 'd3bb13.soap', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())


    if __name__ == '__main__':
        from wsgiref.simple_server import make_server

        wsgi_application = WsgiApplication(application)
        server = make_server('127.0.0.1', 8000, wsgi_application)

        print("D3-BB13 vai te transformar em sabão.")
        server.serve_forever()

