# Stage 1: Build tools and shell in a temporary image
FROM alpine:latest AS build

# Install necessary tools (bash, etc.)
RUN apk add --no-cache bash

# Copy any needed files into this stage
COPY . /app

# Stage 2: Final image
FROM gaiaadm/pumba:master

# Copy tools from the previous stage
COPY --from=build /bin/bash /bin/bash
ENTRYPOINT ["/pumba"]
LABEL Name="WebApp" \
	Version="1.0"
EXPOSE 8082
CMD ["--help"]
