using BCrypt.Net;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
var port = Environment.GetEnvironmentVariable("PORT") ?? "5438";  // if port changed, change in python file too

// Hello World!
app.MapGet("/", () => "Hello World!");

// Sentinel
app.MapPost("/SentinelEn", (SentinelData request) =>
{
    string? key = request.Key;
    string? security = request.Security;
    return SentinelGuard.Encryptor(key, security);
});


// Anti Sentinel
app.MapPost("/SentinelDe", (SentinelData request) =>
{
    string? key = request.Key;
    string? security = request.Security;
    return SentinelGuard.Decryptor(key, security);
});


// Generate a default password
app.MapPost("/Cryotling/Default", (CryoSecureCreatorDefault request) =>
{
    int length = request.Length;
    return CryoSecure.Creator_default(length);
});


// Generate a password from user choice
app.MapPost("/Cryotling/Creator", (CryoSecureCreator request) =>
{
    int length = request.Length;
    bool number = request.Numbers;
    bool special = request.Specials;
    bool upper = request.Upper;
    bool lower = request.Lower;
    return CryoSecure.Creator(length, number, special, upper, lower);
});


// CryoSecure Encryption
app.MapPost("/Cryotling/Encryption", (CryoSecureEncDec request) =>
{
    string? secret = request.Secret;
    int shifts = request.Shifts;
    return CryoSecure.Encryption(secret, shifts);
});
    

// CryoSecure Decryption
app.MapPost("/Cryotling/Decryption", (CryoSecureEncDec request) =>
{
    string? secret = request.Secret;
    int shifts = request.Shifts;
    return CryoSecure.Decryption(secret, shifts);
});

// SentinelGuard CandyCrusher
app.MapPost("/Cryotling/CandyCrusher", (CryoSecureCrusher request) =>
{
    string? secret = request.Secret;
    int workFactor = request.WorkFactor;
    return SentinelGuard.CandyCrusher(secret, workFactor);
});

// SentinelGuard CandyCrusher
app.MapPost("/Cryotling/CandyCrusherChecker", (CryoSecureCrusherChecker request) =>
{
    string? secret = request.Secret;
    string? securely = request.Securely;
    return SentinelGuard.CandyChecker(secret, securely);
});

app.Run($"http://localhost:{port}");


// This help close script from python
Console.CancelKeyPress += (sender, e) =>
{
    e.Cancel = true;  // Prevent the process from terminating immediately
    app.StopAsync().Wait();  // Stop the server gracefully
};


public class SentinelGuard // Secure layer
{
    public static string Encryptor(string? data, string? password)
    {
        if (data == null || password == null)
        {
            return "Error";
        }
        Random random = new Random(password.Sum(c => (int)c));
        char[] obfuscatedData = new char[data.Length];
        for (int i = 0; i < data.Length; i++)
        {
            int randomValue = random.Next(32, 127);
            char obfuscatedChar = (char)(data[i] ^ randomValue);
            obfuscatedData[i] = obfuscatedChar;
        }
        return new string(obfuscatedData);
    }

    public static string Decryptor(string? data, string? password)
    {
        if (data == null || password == null)
        {
            return "Error";
        }
        Random random = new Random(password.Sum(c => (int)c));
        char[] deobfuscatedData = new char[data.Length];
        for (int i = 0; i < data.Length; i++)
        {
            int randomValue = random.Next(32, 127);
            char deobfuscatedChar = (char)(data[i] ^ randomValue);
            deobfuscatedData[i] = deobfuscatedChar;
        }
        return new string(deobfuscatedData);
    }

    public static string CandyCrusher(string? securely, int workFactor = 16)
    {
        if (securely == null)
        {
            return "Error";
        }
        string salt = BCrypt.Net.BCrypt.GenerateSalt(workFactor);
        string hashedPassword = BCrypt.Net.BCrypt.HashPassword(securely, salt);

        return hashedPassword;
    }

    public static bool CandyChecker(string? secret, string? securely)
    {
        if (secret == null || securely == null)
        {
            return false;
        }

        return BCrypt.Net.BCrypt.Verify(secret, securely);
    }

}

public class CryoSecure
{
    public static string Creator(int length, bool number, bool special, bool upper, bool lower)
    // Function to generate the password    
    {
        const string all_numbers = "0123456789";
        const string all_special = "!@#$%?&*()";
        const string all_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        const string all_lower = "abcdefghijklmnopqrstuvwxyz";
        var random = new Random(); 
        var password = new char[length];
        string choosen_characters = "";

        if (number)
        {
            choosen_characters += all_numbers;
        }
        if (special)
        {
            choosen_characters += all_special;
        }
        if (upper)
        {
            choosen_characters += all_upper;
        }
        if (lower)
        {
            choosen_characters += all_lower;
        }

        for (int i =0; i < length; i++) // Loop for the password length
        {
            password[i] = choosen_characters[random.Next(choosen_characters.Length)];
        }

        return new string(password);

    }
    public static string Creator_default(int length)
    // Function to generate the password    
    {
        const string characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%?&*()";
        var random = new Random(); //Initialize random generator 
        var password = new char[length];

        for (int i =0; i < length; i++) // Loop for the password length
        {
            password[i] = characters[random.Next(characters.Length)];
        }

        return new string(password);
    }
    public static string Encryption(string? message, int shift)
    {
        if (message == null)
        {
            return "Error";
        }
        char[] chars = message.ToCharArray();

        for (int i = 0; i < chars.Length; i++)
        {
            if (char.IsLetter(chars[i]))
            {
                char baseChar = char.IsUpper(chars[i]) ? 'A' : 'a';
                chars[i] = (char)(((chars[i] + shift - baseChar) % 26) + baseChar);
            }
        }

        return new string(chars);
    }

    public static string Decryption(string? encryptedMessage, int shift)
    {
        if (encryptedMessage == null)
        {
            return "Error";
        }
        return Encryption(encryptedMessage, 26 - shift); 
    }

}



public class SentinelData
{
    public string? Key { get; set; }
    public string? Security { get; set; }
}

public class CryoSecureCreatorDefault
{
    public int Length { get; set; }
}

public class CryoSecureCreator
{
    public int Length { get; set; }
    public bool Numbers { get; set; }
    public bool Specials { get; set; }
    public bool Upper { get; set; }
    public bool Lower { get; set; }
}

public class CryoSecureEncDec
{
    public string? Secret { get; set; }
    public int Shifts { get; set; }
}

public class CryoSecureCrusher
{
    public string? Secret { get; set; }
    public int WorkFactor { get; set; }
}

public class CryoSecureCrusherChecker
{
    public string? Secret { get; set; }
    public string? Securely { get; set; }
}