# Active Directory Persona Mapping

This short script parses data pulled from Active Directory and performs rudimentary data analysis. Created to speed up data analysis that would have taken at least 10x longer using just Excel.

Below are quick instructions to help get you started.

### PowerShell

You will need to start by pulling AD data using PowerShell (or some other method). Personally, I recommend the following PowerShell script

	Get-ADUser -SearchBase "ou=example,ou=example,dc=example,dc=net" -Filter * -Properties * | Select-Object -Property title, department, physicaldeliveryofficename, @{n='MemberOf'; e= { ( $_.memberof | % { (Get-ADObject $_).Name }) -join ";" }} | Sort-Object -Property | export-CSV C:\temp\example.csv

This will output Job Title, Department, Office, and MemberOf security groups formatted nicely. 

I have also uploaded a sample CSV file for you to take a look at. Your CSV should look similar to the example.