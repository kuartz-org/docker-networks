![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-17ketly3vXpdvvWfaJXp698VXNDUMXjNvw&s)
# Docker Networks
Made by Felipe LOBATO



# <img src="image-1.png" alt="alt text" width="400"/>

- No internet
- Linux machine
- Hard to test
- Hard to deploy
- Limited connection


# 🚀 Why Use Docker?
Docker simplifies application deployment by containerizing software


✅ **Portable**: Run anywhere: local, cloud, or onpremise


✅ **Lightweight**: Uses fewer resources than traditional VMs


✅ **Scalable**: Easily scale services up or down


✅ **Consistent**: Eliminates "works on my machine" problems


✅ **Fast**: Start, stop, and replicate containers in seconds



# 🌐 Docker Networks
_Containers communicating with each other._


## Main types of network:

🔹 **Bridge (default)** – Isolated network for containers to communicate internally.


🔹 **Host** – Containers share the host's network stack.


🔹 **None** – No network (fully isolated).


🔹 **Overlay** – Multi-host communication (Docker Swarm).


🔹 **Macvlan** – Assigns a MAC address, making the container appear as a physical device on the network.



# 📦 Docker Compose & Networking
_Docker Compose simplifies multi-container applications by defining services in a `docker-compose.yml` file_


🛠 **Example (`docker-compose.yml`):**
```yaml
version: "3"
services:
  app:
    image: myapp
    networks:
      - mynetwork
  db:
    image: postgres
    networks:
      - mynetwork

networks:
  mynetwork:
```

👆 Both `app` and `db` can communicate via `mynetwork` without exposing ports externally.



# Let's work!



# Why is better?
# <img src="image-2.png" alt="alt text" width="300"/>