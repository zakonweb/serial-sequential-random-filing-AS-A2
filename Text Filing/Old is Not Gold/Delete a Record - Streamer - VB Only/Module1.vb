Module Module1
    Dim path As String = "C:\Users\Acer\Desktop\ClassData.txt"
    Dim path2 As String = "C:\Users\Acer\Desktop\temp.txt"
    Dim cl As String = ""
    Dim nm As String = ""
    Dim rn As String = ""
    Dim intrn As Integer = 0
    Sub Main()
        Dim roll As String = ""
        Console.Write("Please enter Roll no to be deleted : ")
        roll = Console.ReadLine
        Using sr As System.IO.StreamReader = System.IO.File.OpenText(path)
            Using sw2 As System.IO.StreamWriter = System.IO.File.CreateText(path2)
                cl = sr.ReadLine
                nm = sr.ReadLine
                rn = sr.ReadLine
                intrn = CInt(rn)
                Do While Not rn Is Nothing
                    If roll <> intrn Then
                        sw2.WriteLine(cl)
                        sw2.WriteLine(nm)
                        sw2.WriteLine(rn)
                    End If
                    cl = sr.ReadLine
                    nm = sr.ReadLine
                    rn = sr.ReadLine
                    intrn = CInt(rn)
                Loop
            End Using
        End Using
        System.IO.File.Delete(path)
        My.Computer.FileSystem.RenameFile(path2, "ClassData.txt")
    End Sub

End Module
