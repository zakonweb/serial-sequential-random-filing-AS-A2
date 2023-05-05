Module Module1

    Sub Main()

        Dim rollNo, searchRollNo As Integer
        Dim sName, sContact As String
        Dim sFee As Decimal
        Dim isFeePaid, isFound As Boolean
        isFound = False

        Console.Write("Enter roll number to search for :")
        searchRollNo = Console.ReadLine
        FileOpen(1, "c:\filePractice\sRec.txt", OpenMode.Input)

        While Not EOF(1) And isFound = False
            Input(1, rollNo)
            Input(1, sName)
            Input(1, sContact)
            Input(1, sFee)
            Input(1, isFeePaid)

            If rollNo = searchRollNo Then
                isFound = True

                Console.WriteLine("Student roll no. :" & rollNo)
                Console.WriteLine("Student name :" & sName)
                Console.WriteLine("Student contact :" & sContact)
                Console.WriteLine("Student fee amount :" & sFee)
                Console.WriteLine("Is Fee Paid? " & isFeePaid)
            End If
        End While
        FileClose(1)

        If isFound = False Then Console.WriteLine("Record not found...")


        Console.ReadKey()

    End Sub

End Module
