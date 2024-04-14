set terminal png size 600
set output "prueba_carga.png"
set title "Incremento de cargas, 1000 peticiones, 100 peticiones concurrentes, 200 concurrentes ... 1000 concurrentes"
set size ratio 0.6
set grid y
set xlabel "Nro Peticiones"
set ylabel "Tiempo de respuesta (ms)"
plot "prueba_carga.csv" using 9 smooth sbezier with lines title "http://localhost:8000/api/tasks"
