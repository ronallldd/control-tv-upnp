import upnpclient
import time


device_url = "http://ip:port"


device = upnpclient.Device(device_url)


print("Serviços disponíveis no dispositivo:")
for service in device.services:
    print(f"- {service.service_type}")


try:
    av_transport = device.AVTransport
    print("Serviço AVTransport encontrado!")
except AttributeError:
    print("Serviço AVTransport não encontrado.")
    exit()


try:
    rendering_control = device.RenderingControl
    print("Serviço RenderingControl encontrado!")
except AttributeError:
    print("Serviço RenderingControl não encontrado.")
    exit()


def play_media(media_url):
    av_transport.SetAVTransportURI(
        InstanceID=0,
        CurrentURI=media_url,
        CurrentURIMetaData=""
    )
    print(f"URI da mídia definida: {media_url}")

    av_transport.Play(InstanceID=0, Speed="1")
    print("Reprodução iniciada.")


def set_volume(volume):
    if 0 <= volume <= 100:
        rendering_control.SetVolume(
            InstanceID=0,
            Channel="Master",  
            DesiredVolume=volume
        )
        print(f"Volume definido para: {volume}")
    else:
        print("Volume deve estar entre 0 e 100.")


def get_volume():
    volume = rendering_control.GetVolume(
        InstanceID=0,
        Channel="Master"
    )["CurrentVolume"]
    print(f"Volume atual: {volume}")
    return volume


def get_transport_info():
    transport_info = av_transport.GetTransportInfo(InstanceID=0)
    print("Informações do transporte:")
    for key, value in transport_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
  
    media_url = "http://ip(domain)/video.mp4"

   
    play_media(media_url)

    
    time.sleep(10)

    
    get_transport_info()

    
    set_volume(10)  
    time.sleep(2)

    
    get_volume()

    
    time.sleep(30)

   
    av_transport.Stop(InstanceID=0)
    print("Reprodução parada.")
