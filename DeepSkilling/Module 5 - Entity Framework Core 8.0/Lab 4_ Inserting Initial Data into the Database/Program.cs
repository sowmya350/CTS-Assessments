using RetailInventory.Data;
using RetailInventory.Models;

using var context = new AppDbContext();

// Create Categories
var electronics = new Category
{
    Name = "Electronics"
};

var groceries = new Category
{
    Name = "Groceries"
};

// Add Categories
context.Categories.AddRange(electronics, groceries);

// Create Products
var product1 = new Product
{
    Name = "Laptop",
    Price = 75000,
    Category = electronics
};

var product2 = new Product
{
    Name = "Rice Bag",
    Price = 1200,
    Category = groceries
};

// Add Products
context.Products.AddRange(product1, product2);

// Save to Database
context.SaveChanges();

Console.WriteLine("Data inserted successfully!");