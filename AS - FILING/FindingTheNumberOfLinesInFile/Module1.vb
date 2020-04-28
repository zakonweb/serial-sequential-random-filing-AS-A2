Module Module1

    Sub Main()
        Dim oneLine As String = ""
        Dim lineCounter As Integer = 0

        FileOpen(1, "C:\filePractice\ABC.txt", OpenMode.Input)
        While Not EOF(1)
            Input(1, oneLine)
            lineCounter = lineCounter + 1
        End While

        Console.WriteLine("Number of lines in the file is = " & lineCounter)
        Console.ReadKey()
    End Sub

End Module
