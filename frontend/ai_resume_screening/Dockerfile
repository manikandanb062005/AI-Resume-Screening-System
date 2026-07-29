# ---------- Stage 1: Build the React app ----------
FROM node:20-slim AS builder

WORKDIR /build

# Copy only package files first — this layer gets cached and skipped on rebuilds
# unless dependencies actually change, making iteration much faster
COPY package.json package-lock.json* ./
RUN npm ci

# Now copy the rest of the source and build
COPY . .
RUN npm run build
# Vite outputs to /build/dist by default

# ---------- Stage 2: Serve with Nginx ----------
FROM nginx:1.27-alpine

# Remove default Nginx welcome page config
RUN rm -f /etc/nginx/conf.d/default.conf

# Our custom config: serves the app, proxies /api/* to the backend
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built static files from the build stage
COPY --from=builder /build/dist /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost:80/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
