using System;
using System.Collections.Generic;

namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        {
            IBook book = new DiskBook("David's Gradebook");
            book.GradeAdded += OnGradeAdded;

            EnterGrades(book);

            var stats = book.GetStatistics();

            System.Console.WriteLine($"For the book named {book.Name}");
            System.Console.WriteLine($"The lowest grade is {stats.Low}");
            System.Console.WriteLine($"The highest grade is {stats.High}");
            System.Console.WriteLine($"The average is {stats.Average:N1}");
            System.Console.WriteLine($"The letter grade is {stats.Letter}");
            // book.grades.Add(101); --> illegale bacause grades is a private property of Book
            // in cmd, the command "dotnet run -- David" will pass in "David" into the Main() method
            // no arguments leads do an unhandled exception error due to attempting to access an 
            // index that does not exist (empty array)

            // var x = 34.1;
            // var y = 24.8;
            // var result = x + y;

            // declaring with an input in the array declaration limits the length to exactly that length
            // var numbers = new double[3] {12.7, 10.3, 6.11};
            // numbers[0] = 12.7;
            // numbers[1] = 10.3;
            // numbers[2] = 6.11;
        }

        // we know that we can enter grades to a Book, but we're not sure what will happen to it
        // that is handled by the book class of the variable passed in
        private static void EnterGrades(IBook book)
        {
            while (true)
            {
                System.Console.WriteLine("Enter a grade or 'q' to quit");
                var input = Console.ReadLine();
                if (input == "q")
                {
                    break;
                }

                try
                {
                    var grade = double.Parse(input);
                    book.AddGrade(grade);
                }
                catch (ArgumentException e)
                {
                    System.Console.WriteLine(e.Message);
                }
                catch (FormatException e)
                {
                    System.Console.WriteLine(e.Message);
                }
            }
        }

        static void OnGradeAdded(object sender, EventArgs e)
        {
            System.Console.WriteLine("A grade was added");
        }
    }
}
