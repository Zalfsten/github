# Multi-stage build for a simple Node.js application
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --only=production

# Copy source code
COPY . .

# Production stage
FROM node:18-alpine AS production

# Build argument for app version
ARG APP_VERSION=development

WORKDIR /app

# Install curl for health checks
RUN apk add --no-cache curl

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Copy built application
COPY --from=builder --chown=nodejs:nodejs /app .

# Create a simple app if package.json doesn't exist
RUN if [ ! -f package.json ]; then \
    echo '{"name":"dummy-app","version":"1.0.0","main":"server.js","scripts":{"start":"node server.js"}}' > package.json && \
    echo 'const express = require("express"); const app = express(); app.get("/", (req, res) => res.json({message: "Hello World", version: process.env.APP_VERSION || "unknown"})); app.get("/health", (req, res) => res.json({status: "healthy"})); app.listen(3000, () => console.log("Server running on port 3000"));' > server.js && \
    npm install express; \
    fi

# Set version environment variable
ENV APP_VERSION=${APP_VERSION}

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# Start the application
CMD ["npm", "start"]
