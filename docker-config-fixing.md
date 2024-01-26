It looks like you are encountering issues fetching Ubuntu packages during the Docker build process. The error is related to the inability to connect to the Ubuntu package repository.

### 1. Docker Desktop for Windows

For Docker Desktop on Windows, you can run Linux containers natively without the need for a virtual machine. However, there may be issues with some Linux-specific features. If you are facing problems, you can try the following:

- Ensure that Docker Desktop is running and switch to Linux containers by right-clicking on the Docker icon in the system tray and selecting "Switch to Linux containers."
  
- Modify your Dockerfile to use a different base image. You might consider using a more Windows-friendly image, such as `python:3.6` or another version that fits your requirements.

  ```Dockerfile
  FROM python:3.6
  
  WORKDIR /app
  COPY requirements.txt .
  
  RUN pip install --no-cache-dir -r requirements.txt
  RUN pip install gunicorn==19.9.0
  
  ADD ./backend /app/backend
  ADD ./docker /app/docker
  ADD ./research /app/research
  
  RUN mkdir -p /app/backend/server/static
  ```

### 2. Update Docker Compose

Ensure that your Docker Compose file (`docker-compose.yml`) is correctly configured. Your Docker Compose file looks fine for Linux containers, but if you are using Windows containers, you might need to adjust the configuration accordingly.

### 3. Docker Compose Build Context

Make sure you are running `docker-compose build` from the correct directory. The `context` in your `docker-compose.yml` file specifies where the build context is located. Ensure that you are in the correct directory or adjust the `context` accordingly.

### 4. Check Internet Connection

Ensure that your internet connection is stable, and there are no restrictions or firewalls blocking Docker from accessing external repositories.

### 5. Retry and Use Cache

Sometimes, transient issues might cause the failure. You can try running the build command again using the `--no-cache` option to avoid using the cache from the previous failed build.

```bash
docker-compose build --no-cache
```

### 6. Proxy Settings

If you are behind a proxy, you may need to configure Docker to use the proxy settings. You can do this in the Docker Desktop settings.

### 7. Ubuntu Image

If you still want to use the Ubuntu image, you can try updating the base image tag to a more recent version.

```Dockerfile
FROM ubuntu:20.04
```

After making these adjustments, try running `docker-compose build` again and see if the issue persists.