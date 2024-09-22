# Use multi-stage build to build the frontend

# Use the official bun image
FROM oven/bun:1.0.25 AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file and source code to the working directory
COPY . .

# Install any dependencies
ENV NODE_ENV=production
RUN bun install

# Build the application
RUN bun run build-only

# Use the official Nginx image
FROM nginx:alpine

# Copy the build output to replace the default Nginx contents
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy the Nginx configuration file
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Make port 80 available to the world outside this container
EXPOSE 80

# Run Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
