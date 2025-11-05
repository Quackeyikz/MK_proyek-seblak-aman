# PROYEK SEBLAK AMAN
_The name is so random ngl_

1. Build (execute at project's root folder)
   ```bash
   docker build -t <image-name> -f build/Dockerfile.fixed .
   ```

2. Run in a container
   ```bash
   docker run -d -p 8889:80 --name <container-name> <image-name>
   ```

3. Open in your browser
   [http://localhost:8889](http://localhost:8889)

   Alternatively
   ```bash
   curl localhost:8889
   ```

Any reports, documentation, logs is in the `reports/` folder. Documented screenshots are located in `screenshots/`.
  
  
Written in pain, 
Quackeyikz
