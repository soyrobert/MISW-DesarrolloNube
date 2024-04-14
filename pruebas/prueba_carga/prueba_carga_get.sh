file_content=$(base64 < ../../resources/tests/videos/video_test.mp4)

# Construct the JSON payload
json_payload="{\"file\": \"$file_content\"}"

# Save the JSON payload to a file
echo $json_payload > payload.json

for i in {1..2}; do 
    rate=$((i * 1))  # Incremento en pasos de 100 solicitudes por segundo 
    ab -n 5 -c $rate -T "application/json" -H "Authorization: Bearer $token" -rk -g prueba_carga.csv http://localhost:8000/api/tasks 
done
