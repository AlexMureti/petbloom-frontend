import asyncio
from prisma import Prisma
from datetime import datetime, timedelta

async def seed():
    prisma = Prisma()
    await prisma.connect()
    
    # Comprehensive Pets Data with Kenyan Shillings (KES)
    pets_data = [
        # DOGS
        {"name": "Max", "species": "dogs", "breed": "Golden Retriever", "age": 2, "weight": 30, "description": "Friendly and energetic golden retriever with beautiful cream coat. Perfect for active families. Fully vaccinated and dewormed.", "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400", "https://images.unsplash.com/photo-1558788353-f76d92427f16?w=400"], "videos": ["https://example.com/max-video.mp4"], "personality": ["friendly", "energetic", "loyal"], "breederName": "Golden Dreams Kennel", "breederRating": 4.8, "price": 95000.00, "available": True},
        {"name": "Buddy", "species": "dogs", "breed": "Labrador Retriever", "age": 3, "weight": 35, "description": "Playful chocolate Labrador with excellent temperament. Great with children and other pets. Trained basic commands.", "images": ["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"], "videos": [], "personality": ["playful", "loyal", "intelligent"], "breederName": "Happy Paws", "breederRating": 4.7, "price": 85000.00, "available": True},
        {"name": "Rocky", "species": "dogs", "breed": "German Shepherd", "age": 1, "weight": 28, "description": "Strong and intelligent German Shepherd. Alert and protective family guardian. Excellent bloodline, trained for obedience.", "images": ["https://images.unsplash.com/photo-1568572933382-74d440642117?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"], "videos": [], "personality": ["intelligent", "protective", "loyal"], "breederName": "Shepherd Elite", "breederRating": 4.9, "price": 110000.00, "available": True},
        {"name": "Charlie", "species": "dogs", "breed": "Beagle", "age": 2, "weight": 12, "description": "Small but mighty Beagle with excellent hunting instincts. Friendly and curious personality. Great for apartment living.", "images": ["https://images.unsplash.com/photo-1505628346881-b72b27e84530?w=400"], "videos": [], "personality": ["friendly", "curious", "energetic"], "breederName": "Beagle House", "breederRating": 4.6, "price": 65000.00, "available": True},
        {"name": "Duke", "species": "dogs", "breed": "Rottweiler", "age": 4, "weight": 50, "description": "Magnificent Rottweiler with calm temperament. Despite reputation, very affectionate and family-oriented. Well-trained.", "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"], "videos": [], "personality": ["calm", "loyal", "protective"], "breederName": "Noble Rotts", "breederRating": 4.8, "price": 120000.00, "available": True},
        
        # CATS
        {"name": "Whiskers", "species": "cats", "breed": "Persian", "age": 1, "weight": 4.5, "description": "Elegant and refined Persian cat with luxurious long coat. Calm and affectionate. Requires regular grooming.", "images": ["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"], "videos": [], "personality": ["calm", "affectionate", "elegant"], "breederName": "Purrfect Cats", "breederRating": 4.9, "price": 55000.00, "available": True},
        {"name": "Luna", "species": "cats", "breed": "Siamese", "age": 2, "weight": 3.2, "description": "Beautiful Siamese with striking blue eyes. Vocal and interactive. Loves attention and playtime.", "images": ["https://images.unsplash.com/photo-1513360371669-4a8e1949883e?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"], "videos": [], "personality": ["vocal", "playful", "affectionate"], "breederName": "Siamese Dreams", "breederRating": 4.8, "price": 48000.00, "available": True},
        {"name": "Shadow", "species": "cats", "breed": "Black Domestic Shorthair", "age": 3, "weight": 4.0, "description": "Sleek black cat with golden eyes. Independent but loving. Perfect for quiet homes. Excellent mouser.", "images": ["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"], "videos": [], "personality": ["independent", "loving", "intelligent"], "breederName": "Shadow's Sanctuary", "breederRating": 4.7, "price": 35000.00, "available": True},
        {"name": "Mittens", "species": "cats", "breed": "British Shorthair", "age": 2, "weight": 5.5, "description": "Plump and cuddly British Shorthair with grey coat. Very calm and sociable. Great family pet.", "images": ["https://images.unsplash.com/photo-1567517381829-ba595fac2ec0?w=400"], "videos": [], "personality": ["calm", "sociable", "cuddly"], "breederName": "British Beauties", "breederRating": 4.9, "price": 52000.00, "available": True},
        {"name": "Tiger", "species": "cats", "breed": "Orange Tabby", "age": 1, "weight": 3.8, "description": "Energetic and playful orange tabby. Full of personality and mischief. Loves interactive toys.", "images": ["https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400"], "videos": [], "personality": ["playful", "energetic", "mischievous"], "breederName": "Tabby House", "breederRating": 4.6, "price": 40000.00, "available": True},
    ]
    
    # Comprehensive Products Data with Kenyan Shillings (KES)
    products_data = [
        # DOG FOOD
        {"name": "Premium Adult Dog Food", "description": "High-quality dry dog food with balanced nutrition. Rich in protein and essential vitamins. Suitable for all dog breeds.", "category": "food", "petType": "dogs", "brand": "PetPro", "price": 3500.00, "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], "stock": 50, "filters": ["adult", "nutritious"]},
        {"name": "Grain-Free Puppy Food", "description": "Specially formulated for puppies. No grains, rich in DHA for brain development. Supports healthy growth.", "category": "food", "petType": "dogs", "brand": "NutriPaws", "price": 4200.00, "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], "stock": 35, "filters": ["puppy", "grain-free"]},
        {"name": "Senior Dog Food", "description": "Low-calorie formula for senior dogs. Easy to digest with joint support ingredients.", "category": "food", "petType": "dogs", "brand": "GoldenYears", "price": 3800.00, "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], "stock": 25, "filters": ["senior", "low-calorie"]},
        
        # CAT FOOD
        {"name": "Premium Cat Food - Salmon", "description": "Delicious salmon flavor cat food. Complete nutrition for adult cats. Promotes healthy coat.", "category": "food", "petType": "cats", "brand": "FelineFresh", "price": 2800.00, "images": ["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"], "stock": 40, "filters": ["salmon", "adult"]},
        {"name": "Kitten Growth Formula", "description": "Specially designed for kittens aged 2-12 months. High protein for development.", "category": "food", "petType": "cats", "brand": "KittyStart", "price": 3200.00, "images": ["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"], "stock": 30, "filters": ["kitten", "growth"]},
        
        # DOG TOYS
        {"name": "Interactive Dog Toy Set", "description": "Set of 5 interactive toys to keep dogs entertained. Includes balls, ropes, and chew toys.", "category": "toys", "petType": "dogs", "brand": "PlayPets", "price": 2200.00, "images": ["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"], "stock": 45, "filters": ["interactive", "durable"]},
        {"name": "Durable Rope Tug Toy", "description": "Strong rope toy for aggressive chewers. Great for multi-dog families. Machine washable.", "category": "toys", "petType": "dogs", "brand": "ChewMaster", "price": 1500.00, "images": ["https://images.unsplash.com/photo-1535241749838-299277b6305f?w=400"], "stock": 50, "filters": ["rope", "durable"]},
        {"name": "Dog Puzzle Feeder", "description": "Keep your dog mentally stimulated. Improves problem-solving skills during feeding time.", "category": "toys", "petType": "dogs", "brand": "BrainPlay", "price": 2800.00, "images": ["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"], "stock": 20, "filters": ["puzzle", "mental-stimulation"]},
        
        # CAT TOYS
        {"name": "Feather Wand Cat Toy", "description": "Interactive feather wand toy. Stimulates hunting instincts. Great for exercise.", "category": "toys", "petType": "cats", "brand": "CatPlay", "price": 800.00, "images": ["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"], "stock": 60, "filters": ["interactive", "feather"]},
        {"name": "Cat Laser Toy", "description": "Safe laser toy for cats. Promotes exercise and play. Includes auto-timer feature.", "category": "toys", "petType": "cats", "brand": "LaserFun", "price": 1200.00, "images": ["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"], "stock": 30, "filters": ["laser", "interactive"]},
        
        # HABITATS
        {"name": "Deluxe Cat Bed", "description": "Soft and comfortable cat bed. Machine washable cover. Cozy cave design.", "category": "habitats", "petType": "cats", "brand": "CatsLounge", "price": 4500.00, "images": ["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"], "stock": 25, "filters": ["comfortable", "cave"]},
        {"name": "Multi-Level Cat Tree", "description": "5-level cat tree with scratching posts. Provides climbing and resting areas. Sturdy construction.", "category": "habitats", "petType": "cats", "brand": "CatsLounge", "price": 12000.00, "images": ["https://images.unsplash.com/photo-1521568547814-0a0a0d8a2d3a?w=400"], "stock": 10, "filters": ["climbing", "scratching-posts"]},
        
        # ACCESSORIES
        {"name": "Premium Dog Collar with Leash", "description": "Adjustable leather collar with matching leash. Comfortable and durable. Multiple sizes.", "category": "accessories", "petType": "dogs", "brand": "SafeGuard", "price": 2500.00, "images": ["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"], "stock": 35, "filters": ["leather", "adjustable"]},
        {"name": "Cat Harness and Leash Set", "description": "Lightweight and safe harness for cats. Perfect for outdoor walks. Escape-proof design.", "category": "accessories", "petType": "cats", "brand": "SafeGuard", "price": 1800.00, "images": ["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"], "stock": 20, "filters": ["lightweight", "safe"]},
        
        # GROOMING
        {"name": "Professional Dog Grooming Kit", "description": "Complete grooming set including clippers, scissors, and brush. Suitable for all coat types.", "category": "grooming", "petType": "dogs", "brand": "GroomPro", "price": 5500.00, "images": ["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"], "stock": 15, "filters": ["professional", "complete"]},
        {"name": "Cat Grooming Brush", "description": "Gentle de-matting brush for cats. Reduces shedding. Comfortable grip handle.", "category": "grooming", "petType": "cats", "brand": "GroomPro", "price": 1500.00, "images": ["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"], "stock": 40, "filters": ["gentle", "de-matting"]},
    ]
    
    # Clear existing data
    await prisma.review.delete_many()
    await prisma.message.delete_many()
    await prisma.useraddress.delete_many()
    await prisma.product.delete_many()
    await prisma.pet.delete_many()
    
    # Create pets
    pets = []
    for pet in pets_data:
        created_pet = await prisma.pet.create(data=pet)
        pets.append(created_pet)
        print(f"✅ Created pet: {pet['name']}")
    
    # Create products
    products = []
    for product in products_data:
        created_product = await prisma.product.create(data=product)
        products.append(created_product)
        print(f"✅ Created product: {product['name']}")
    
    # Create comprehensive reviews for products
    review_data = [
        {"userId": "user_001", "productId": products[0].id if len(products) > 0 else None, "rating": 5, "comment": "Excellent quality! My dog loves this food. Great value for money in KES."},
        {"userId": "user_002", "productId": products[0].id if len(products) > 0 else None, "rating": 4, "comment": "Good product, my dogs have shinier coats now."},
        {"userId": "user_003", "productId": products[0].id if len(products) > 0 else None, "rating": 5, "comment": "Worth every shilling! Highly recommended."},
        {"userId": "user_001", "productId": products[1].id if len(products) > 1 else None, "rating": 5, "comment": "Perfect for my puppy. Growing well with this food."},
        {"userId": "user_004", "productId": products[2].id if len(products) > 2 else None, "rating": 4, "comment": "Durable and my dog enjoys the variety of toys."},
        {"userId": "user_005", "productId": products[4].id if len(products) > 4 else None, "rating": 5, "comment": "My cat goes crazy for the salmon flavor!"},
        {"userId": "user_006", "productId": products[7].id if len(products) > 7 else None, "rating": 5, "comment": "Best interactive toy ever. Keeps my dog busy for hours."},
    ]
    
    for review in review_data:
        if review["productId"]:
            created_review = await prisma.review.create(data=review)
            print(f"✅ Created product review: {review['comment'][:50]}...")
    
    # Create reviews for pets
    pet_review_data = [
        {"userId": "user_001", "petId": pets[0].id if len(pets) > 0 else None, "rating": 5, "comment": "Max is absolutely amazing! Perfect temperament and beautiful coat."},
        {"userId": "user_002", "petId": pets[0].id if len(pets) > 0 else None, "rating": 5, "comment": "Worth every shilling. Great family pet!"},
        {"userId": "user_003", "petId": pets[1].id if len(pets) > 1 else None, "rating": 5, "comment": "Buddy is the sweetest. Great breeder!"},
        {"userId": "user_004", "petId": pets[2].id if len(pets) > 2 else None, "rating": 5, "comment": "Rocky is intelligent and loyal. Best decision!"},
        {"userId": "user_005", "petId": pets[4].id if len(pets) > 4 else None, "rating": 4, "comment": "Duke is calm and protective. Great addition to family."},
    ]
    
    for review in pet_review_data:
        if review["petId"]:
            created_review = await prisma.review.create(data=review)
            print(f"✅ Created pet review: {review['comment'][:50]}...")
    
    # Create sample user addresses
    addresses_data = [
        {
            "userId": "user_001",
            "street": "123 Kenyatta Avenue",
            "city": "Nairobi",
            "state": "Nairobi County",
            "zipCode": "00100",
            "country": "Kenya",
            "isDefault": True
        },
        {
            "userId": "user_001",
            "street": "456 Moi Road",
            "city": "Mombasa",
            "state": "Coast County",
            "zipCode": "80100",
            "country": "Kenya",
            "isDefault": False
        },
        {
            "userId": "user_002",
            "street": "789 Ahmed Gaddafi Lane",
            "city": "Nairobi",
            "state": "Nairobi County",
            "zipCode": "00600",
            "country": "Kenya",
            "isDefault": True
        },
        {
            "userId": "user_003",
            "street": "321 Ring Road",
            "city": "Kisumu",
            "state": "Kisumu County",
            "zipCode": "40100",
            "country": "Kenya",
            "isDefault": True
        },
    ]
    
    for address in addresses_data:
        created_address = await prisma.useraddress.create(data=address)
        print(f"✅ Created address: {address['city']}, {address['street']}")
    
    # Create sample messages
    messages_data = [
        {
            "senderId": "user_002",
            "recipientId": "user_001",
            "content": "Hi! I'm very interested in Max the Golden Retriever. Is he still available? When can we arrange a viewing?"
        },
        {
            "senderId": "user_001",
            "recipientId": "user_002",
            "content": "Yes, Max is available! We can arrange a viewing this weekend. What time works best for you?"
        },
        {
            "senderId": "user_003",
            "recipientId": "user_001",
            "content": "Interested in Rocky the German Shepherd. What is the current price in KES?"
        },
        {
            "senderId": "user_001",
            "recipientId": "user_003",
            "content": "Rocky is priced at KES 110,000. He's a wonderful dog with excellent bloodline!"
        },
        {
            "senderId": "user_004",
            "recipientId": "user_001",
            "content": "Do you have any Siamese cats available? Particularly interested in Luna."
        },
        {
            "senderId": "user_001",
            "recipientId": "user_004",
            "content": "Yes! Luna is available at KES 48,000. She's very interactive and loving!"
        },
    ]
    
    for msg in messages_data:
        created_msg = await prisma.message.create(data=msg)
        print(f"✅ Created message: {msg['content'][:50]}...")
    
    print("\n" + "="*60)
    print("✅ DATABASE SEEDED SUCCESSFULLY!")
    print("="*60)
    print(f"   📊 SUMMARY:")
    print(f"   🐕 Pets: {len(pets)}")
    print(f"      - Dogs: 5")
    print(f"      - Cats: 5")
    print(f"   📦 Products: {len(products)}")
    print(f"      - Food: 5")
    print(f"      - Toys: 5")
    print(f"      - Habitats: 2")
    print(f"      - Accessories: 2")
    print(f"      - Grooming: 2")
    print(f"   ⭐ Product Reviews: {len([r for r in review_data if r['productId']])}")
    print(f"   ⭐ Pet Reviews: {len(pet_review_data)}")
    print(f"   📍 Addresses: {len(addresses_data)}")
    print(f"   💬 Messages: {len(messages_data)}")
    print("="*60)
    print("💰 Currency: All prices in Kenyan Shillings (KES)")
    print("="*60)
    await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(seed())
