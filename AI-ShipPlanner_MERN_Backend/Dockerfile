# Use official Node.js runtime
FROM node:18

# Set working directory inside container
WORKDIR /app

# Copy package files first (better caching for Docker layers)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the source code
COPY . .

# Expose backend port
EXPOSE 8000

# Start the app
CMD ["npm", "start"]
