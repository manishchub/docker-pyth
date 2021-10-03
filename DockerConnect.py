import docker
client = docker.from_env()

image_list=client.images.list()
image_list_ver=[]

for images in image_list:
    image_name=tuple(str(images).split(":"))
    image_ver=(image_name[1].replace("'","")+":"+image_name[2].replace(">","").replace("'",""))
    image_list_ver.append(image_ver.strip())

print(image_list_ver)

print('Creating container...')

for img in image_list_ver:
    client.containers.run(image=img,detach=True)

for cont in client.containers.list():
    print(cont)

print('Stopping containers...')

for cont in client.containers.list():
    cont_obj=client.containers.get(cont.id)
    cont_obj.stop()
    cont_obj.reload()
    print(cont_obj.attrs['Name'] + " " + cont_obj.attrs['State']['Status'])

client.containers.prune()
print('Containers succesfully stopped...')




# print(image_list)

# client.login(username='montish',password='Docker@2019',registry='https://index.docker.io/v1/')
# client.images.pull('nginx')
# image_list=tuple(client.images.list())
# print(image_list)
#
#
# print('running the containers')
# #client.containers.run('', 'echo hello world')
#
