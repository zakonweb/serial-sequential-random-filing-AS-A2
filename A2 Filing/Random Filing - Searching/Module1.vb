Module Module1

    Structure sRecType
        Dim rollNo As Integer
        <VBFixedString(25)> Dim sName As String
        <VBFixedString(16)> Dim sContact As String
        Dim sFee As Decimal
        Dim isFeePaid As Boolean
    End Structure

    Sub Main()
        Dim myRec As sRecType
        Dim NoOfRecs As Integer
        Dim recPos As Integer
        Dim searchNo As Integer
        Dim isFound As Boolean = False

        Console.Write("Enter No. to search for: ")
        searchNo = Console.ReadLine

        FileOpen(1, "D:\filePractice\sRecRandom", _
                 OpenMode.Random, OpenAccess.ReadWrite, , _
                 Len(myRec))

        NoOfRecs = (LOF(1) / Len(myRec))

        For recPos = 1 To NoOfRecs
            FileGet(1, myRec, recPos)
            If myRec.rollNo = searchNo Then
                isFound = True

                Console.WriteLine("Roll no: " & myRec.rollNo)
                Console.WriteLine("Student name: " & myRec.sName)
                Console.WriteLine("Student contact: " & myRec.sContact)
                Console.WriteLine("Fee amount: " & myRec.sFee)
                Console.WriteLine("Is fee paid? " & myRec.isFeePaid)
            End If

            If isFound = True Then Exit For
        Next

        If isFound = False Then Console.WriteLine("Record not found.")
        Console.ReadKey()
        FileClose(1)

    End Sub

End Module
