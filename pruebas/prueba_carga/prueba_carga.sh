for i in {1..2}; do 
    rate=$((i * 100))  # Incremento en pasos de 100 solicitudes por segundo 
    ab -n 1000 -c $rate -p post_data.txt -T "multipart/form-data; boundary=1234567890" -H "Authorization: Bearer $token" -rk -g prueba_carga.csv http://localhost:8000/api/tasks 
done
