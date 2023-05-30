if [ -z $DISCORD_TOKEN ]; then
    echo "DISCORD_TOKEN required"
    exit 1
fi

vxbot --token $DISCORD_TOKEN
