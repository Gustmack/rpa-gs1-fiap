import datetime

def process_temperature_data(json_data):
    try:
        current_year = str(datetime.date.today().year)  # Definir o ano corrente como inteiro
        # Converter JSON para lista de dicionários manualmente
        data = eval(json_data)
        
        # Definir o limiar de anomalia (por exemplo, 30 graus)
        anomaly_threshold = 30.0

        # Encontrar o registro do ano corrente
        current_year_record = None
        for record in data:
            if record["Year"] == current_year:
                current_year_record = record
                break
        
        if not current_year_record:
            return "Ano corrente não encontrado nos dados"

        # Obter o último valor válido (excluindo o campo 'Year')
        last_day_key = None
        last_temp = None
        max_day = 0
        for key in current_year_record.keys():
            if key.startswith("Day_"):
                day_number = int(key.split('_')[1])
                temp_str = current_year_record[key]
                try:
                    temp = float(temp_str) if temp_str else None
                except ValueError:
                    temp = None
                if temp is not None and day_number > max_day:
                    max_day = day_number
                    last_day_key = key
                    last_temp = temp

        if last_day_key is None:
            return "Nenhum dado de temperatura válido encontrado para o ano corrente"

        # Verificar se o último valor é uma anomalia
        is_anomaly = last_temp > anomaly_threshold

        # Retornar apenas o valor booleano da anomalia
        return str(is_anomaly)
    except Exception as e:
        return str(e)