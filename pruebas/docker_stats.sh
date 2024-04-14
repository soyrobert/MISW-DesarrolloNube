#!/bin/bash

# Define the filename to save the stats
output_file="docker_stats.txt"

# Run the loop continuously
while true; do
    # Get the current date and time
    current_date=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Execute docker stats without streaming
    docker_stats_output=$(docker stats --no-stream)
    
    # Check if the output is not empty
    if [ -n "$docker_stats_output" ]; then
        # If not empty, append the date and output to the file
        echo "$current_date" >> "$output_file"
        echo "$docker_stats_output" >> "$output_file"
    fi
    
    # Wait for 1 second before the next iteration
    sleep 1
done

