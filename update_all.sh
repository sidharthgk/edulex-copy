#!/bin/bash

# Colors for styling
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================"
echo -e "Updating Combined Repository and Subtrees"
echo -e "========================================${NC}"

echo -e "${YELLOW}Pulling updates for the combined repo...${NC}"
git pull origin main && echo -e "${GREEN}Combined repo updated successfully!${NC}"

repos=(
  "dyslexia-detection-api git@github.com:edulex/detection-api.git main"
  "backend git@github.com:edulex/backend.git main"
  "landing git@github.com:edulex/landing.git prod" # Use prod branch for landing
  "app git@github.com:edulex/app.git main"
)

for repo in "${repos[@]}"; do
  prefix=$(echo $repo | cut -d ' ' -f 1)
  url=$(echo $repo | cut -d ' ' -f 2)
  branch=$(echo $repo | cut -d ' ' -f 3)
  echo -e "${YELLOW}Pulling updates for $prefix (branch: $branch)...${NC}"
  git subtree pull --prefix=$prefix $url $branch && \
  echo -e "${GREEN}$prefix (branch: $branch) updated successfully!${NC}" || \
  echo -e "${RED}Failed to update $prefix (branch: $branch)! Check for errors.${NC}"
done

echo -e "${BLUE}========================================"
echo -e "All repositories updated successfully!"
echo -e "========================================${NC}"
