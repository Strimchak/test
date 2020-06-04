FROM mcr.microsoft.com/mssql/server:2017-latest
 
        ENV ACCEPT_EULA=Y
        ENV SA_PASSWORD=StrongP@ssw0rd
	ENV MSSQL_TCP_PORT=1433 
