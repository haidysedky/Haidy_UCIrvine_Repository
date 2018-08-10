Sub Stock_Market_Prod():
'---Building Easy Section Variables
Dim Ticker_Row As Integer
Dim Total_Volume As Double
'---Building Moderate Section Variables
Dim Year_Close As Double
Dim Year_Open As Double
Dim Yearly_Change As Double
Dim Percent_Change As Double
'---Building Hard Section Variables
Dim Greatest_Increase As Double
Dim Greatest_Decrease As Double
Dim Greatest_Volume As Double
Dim Greatest_Increase_Ticker As String
Dim Greatest_Decrease_Ticker As String
Dim Greatest_Volume_Ticker As String

For Each ws In Worksheets

    Lastrow = Cells(Rows.Count, 1).End(xlUp).Row
    
    Total_Volume = 0
    Ticker_Row = 2
    
    ws.Cells(1, 9) = "Ticker"
    ws.Cells(1, 10) = "Total_Volume"
    ws.Cells(1, 11) = "Yearly_Change"
    ws.Cells(1, 12) = "Percent_Change"
    
    For i = 2 To Lastrow
    
        '---Moderate Section Calculate Year Open
        If ws.Cells(i - 1, 1).Value <> ws.Cells(i, 1).Value Then
        Year_Open = ws.Cells(i, 3).Value
        End If
        
        '---easy + Moderate section
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        
        ws.Cells(Ticker_Row, 9).Value = ws.Cells(i, 1).Value '---Assign Ticker Name
        
        Total_Volume = Total_Volume + ws.Cells(i, 7).Value '---Calculate Total Volume
        ws.Cells(Ticker_Row, 10).Value = Total_Volume  '---Assign Total Volume
        
        Year_Close = ws.Cells(i, 6).Value  '---Moderate Section Calculate Closing Volume
        Yearly_Change = Year_Close - Year_Open '---Moderate Section Calculate Yearly Change
        ws.Cells(Ticker_Row, 11).Value = Yearly_Change  '---Moderate Section Assign Yearly Change
        '---ws.Cells(Ticker_Row, 11).NumberFormat = "00.00000000" '---Format the number
        
        If (Year_Open = 0) Then
        Percent_Change = 0
        Else: Percent_Change = (Yearly_Change / Year_Open)
        End If
        '---Moderate Section Calculate Percent Change
        ws.Cells(Ticker_Row, 12) = Percent_Change '---Moderate Section Assign Percent Change
        Ticker_Row = Ticker_Row + 1
        
        Total_Volume = 0
        '---the code is supposed to work the same if i remove the following 4 lines i just added them for better understanding
        Yearly_Change = 0
        Year_Close = 0
        Year_Open = 0
        Percent_Change = 0
        Else
        
        Total_Volume = Total_Volume + ws.Cells(i, 7).Value
    
        End If
    Next i
    
    Greatest_Increase = 0 '---I supposed the HW means for each WS like for all the other requirements as well as my numbers matched the given ones
    Greatest_Decrease = 0
    Greatest_Volume = 0
    
    Lastrow_Summary = ws.Cells(Rows.Count, 9).End(xlUp).Row
    For i = 2 To Lastrow_Summary
       '---Conditinal Formatting / Moderate Section
        If ws.Cells(i, 11).Value < 0 Then
        ws.Cells(i, 11).Interior.ColorIndex = 3
        ElseIf ws.Cells(i, 11).Value > 0 Then
        ws.Cells(i, 11).Interior.ColorIndex = 4
        End If
        '---Formatting as Percentage
        ws.Range("L2:L" & Lastrow_Summary).NumberFormat = "0.00%"
        '---Hard Section
        ws.Range("O2").Value = "Greatest % Increase"
        ws.Range("O3").Value = "Greatest % Decrease"
        ws.Range("O4").Value = "Greatest Total Volume"
        ws.Range("P1").Value = "Ticker"
        ws.Range("Q1").Value = "Value"
    
        If ws.Cells(i, 12).Value >= Greatest_Increase Then
        Greatest_Increase = ws.Cells(i, 12).Value
        Greatest_Increase_Ticker = ws.Cells(i, 9).Value
        End If
    
        If ws.Cells(i, 12).Value <= Greatest_Decrease Then
        Greatest_Decrease = ws.Cells(i, 12).Value
        Greatest_Decrease_Ticker = ws.Cells(i, 9).Value
        End If
    
        If ws.Cells(i, 10).Value >= Greatest_Volume Then
        Greatest_Volume = ws.Cells(i, 10).Value
        Greatest_Volume_Ticker = ws.Cells(i, 9).Value
        End If
        
    Next i
    ws.Range("Q2").Value = Greatest_Increase
    ws.Range("P2").Value = Greatest_Increase_Ticker
    ws.Range("Q3").Value = Greatest_Decrease
    ws.Range("P3").Value = Greatest_Decrease_Ticker
    ws.Range("Q4").Value = Greatest_Volume
    ws.Range("P4").Value = Greatest_Volume_Ticker
    '---Formatting as Percentage
    ws.Range("Q2:Q3").NumberFormat = "0.00%"
    
ws.Columns("A:Q").AutoFit
Next ws
    
End Sub

