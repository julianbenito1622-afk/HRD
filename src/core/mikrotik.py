import librouteros

class MikroTik:
    def __init__(self, host, user, password, port=8728):
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def conectar(self):
        return librouteros.connect(
            host=self.host,
            username=self.user,
            password=self.password,
            port=self.port
        )

    def cortar_cliente(self, ip):
        api = self.conectar()
        api('/ip/firewall/address-list/add', 
            list='bloqueados', 
            address=ip,
            comment='HRD-bloqueado'
        )
        api.close()
        return {"status": "cortado", "ip": ip}

    def activar_cliente(self, ip):
        api = self.conectar()
        reglas = api('/ip/firewall/address-list/print', 
            **{'?list': 'bloqueados', '?address': ip}
        )
        for regla in reglas:
            api('/ip/firewall/address-list/remove', 
                **{'.id': regla['.id']}
            )
        api.close()
        return {"status": "activado", "ip": ip}

    def listar_conectados(self):
        api = self.conectar()
        clientes = api('/ip/dhcp-server/lease/print')
        resultado = [
            {
                "ip": c.get("address"),
                "mac": c.get("mac-address"),
                "hostname": c.get("host-name", "")
            }
            for c in clientes
        ]
        api.close()
        return resultado