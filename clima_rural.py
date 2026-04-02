import requests, os
decision = True

input("* * * * * * * * * * * * - Bem-vindo ao: Clima Rural - * * * * * * * * * * * *" \
    "\nNesse sistema, você ficará por dentro de como está o tempo na região do " \
    "CEAGRI-2.\nTambém será mostrada a previsão do tempo para o restante do dia." \
    "\nPressione Enter para prosseguir com a sua solicitação.")

while True:
    try: 
        response = requests.get(url = "https://api.open-meteo.com/v1/forecast?latitude=-8.017578&longitude=-34.944705&daily=temperature_2m_max," \
        "temperature_2m_min,precipitation_sum&hourly=rain,temperature_2m,apparent_temperature,precipitation_probability," \
        "precipitation&current=temperature_2m,apparent_temperature,relative_humidity_2m,precipitation&timezone=America%2FSao_Paulo&forecast_days=1")
        data = response.json()
        precipitation_sum = data["daily"]["precipitation_sum"]

    except:
        print("Você está sem conexão no momento ou o servidor não respondeu corretamente. Tente novamente mais tarde.")
        break

    os.system("cls")
    print("* * * * * * * * * * * * - Bem-vindo ao: Clima Rural - * * * * * * * * * * * *")
    print(f"A hora atual é: {data["current"]["time"][11::]}"
        "\nAs informações atuais são:"
        f"\nA temperatura atual é: {data["current"]["temperature_2m"]}Cº"
        f"\nA sensação térmica é de: {data["current"]["apparent_temperature"]}Cº"
        f"\nO índice de umidade atual é: {data["current"]["relative_humidity_2m"]}%"
        "\nA previsão ao longo do dia é:"
        f"\nA temperatura máxima é de: {data["daily"]["temperature_2m_max"][0]}Cº"
        f"\nA temperatura mínima é de: {data["daily"]["temperature_2m_min"][0]}Cº"
        )

    if float(*precipitation_sum) >= 40.00:
        print(f"Opa! Tome cuidado, vai chover muito. O previsto ao longo do dia é de: {float(*precipitation_sum)}mm" \
        "\nConfira com a universidade ou com o seu professor se as aulas estão mantidas.")

    elif float(*precipitation_sum) >= 20.00:
        print("Se ligue, vai chover um volume considerável ao longo do dia, " 
            f"\nO previsto ao longo do dia é de: {float(*precipitation_sum)}mm"
            "\ntome cuidado.")

    elif float(*precipitation_sum) > 0.00:
        print("Vai chover, mas não muito, ufa! Continue atento à previsão. " 
            f"\nO previsto ao longo do dia é de: {float(*precipitation_sum)}mm.")

    else:
        print("Maravilha! Hoje não há previsão de chuva. Você pode pegar o seu Tancredo " \
        "\nNeves - Macaxeira sem medo de se molhar da parada da LAFEPE até o CEAGRI-2.")
    
    print("Você deseja atualizar as informações? Um novo request será feito ao servidor." \
    "\n[S] para sim" \
    "\n[N] para não")

    while True:
        option = input().strip().upper()
        if option in ("S", "N"):
            break

        print("Por favor, digite uma opção válida."
        "\n[S] para sim"
        "\n[N] para não")

    if option == "S":
        continue
    
    else:
        print("Obrigado por checar a previsão climática comigo, tenha uma boa ida à universidade!")
        break