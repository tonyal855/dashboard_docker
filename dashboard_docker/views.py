from django.shortcuts import render
from django.http import HttpResponseRedirect
import docker

client = docker.from_env()

def index(request):
    if request.method == 'POST':
        print()
        image = request.POST['image']
        port_cont = request.POST['port_container']
        port_host  = request.POST['port_host']
        try:
            client.containers.create(image=image, ports={'{}/tcp'.format(port_cont): int(port_host)})
        except:
            client.images.pull("{}:latest".format(image))
            client.containers.create(image=image, ports={'{}/tcp'.format(port_cont): int(port_host)})

        return HttpResponseRedirect('/')
    else:
        res = []
        for container in client.containers.list(all=True):
            cont = {}
            cont['id'] = container.id
            cont['image'] = container.image
            cont['status'] = container.status
            cont['ports'] = container.ports
            res.append(cont)

        return render(request, 'index.html', {'data': res})

def start(request):
    id = request.GET['id']
    cont = client.containers.get(id)
    cont.start()

    return HttpResponseRedirect('/')

def stop(request):
    id = request.GET['id']
    cont = client.containers.get(id)
    cont.stop()

    return HttpResponseRedirect('/')

def delete(request):
    id = request.GET['id']
    cont = client.containers.get(id)
    cont.remove()

    return HttpResponseRedirect('/')

def get_images(request):
    res = []
    for image in client.images.list():
        img = {}
        img['image'] = image
        res.append(img)

    return render(request, 'get_images.html', {'data': res})

