from fastapi import APIRouter, HTTPException
from app.services.prisma_client import prisma_client
import subprocess
import os

router = APIRouter(prefix="/seed", tags=["seed"])

@router.post("/clear")
async def clear_database():
    """Clear all data from database"""
    try:
        await prisma_client.cartitem.delete_many()
        await prisma_client.wishlist.delete_many()
        await prisma_client.orderitem.delete_many()
        await prisma_client.order.delete_many()
        await prisma_client.pet.delete_many()
        await prisma_client.product.delete_many()
        await prisma_client.user.delete_many()
        return {"message": "✅ Database cleared successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Clear failed: {str(e)}")
async def init_schema():
    """Initialize database schema using Prisma"""
    try:
        # Run prisma db push to create tables
        result = subprocess.run(
            ["prisma", "db", "push", "--skip-generate"],
            cwd=os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            return {"message": "Schema initialized", "details": result.stdout}
        
        return {"message": "✅ Schema initialized successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Schema init failed: {str(e)}")

@router.post("/init")
async def seed_database():
    """Initialize database with comprehensive sample data in Kenyan Shillings"""
    try:
        # Check if data already exists
        existing_products = await prisma_client.product.find_many(take=1)
        if existing_products:
            return {"message": "Database already seeded"}
        
        # Comprehensive Pets Data with Kenyan Shillings (KES)
        pets_data = [
            # DOGS
            {
                "name": "Max",
                "species": "dogs",
                "breed": "Golden Retriever",
                "age": 2,
                "weight": 30.0,
                "description": "Friendly and energetic golden retriever with beautiful cream coat. Perfect for active families. Fully vaccinated and dewormed.",
                "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400", "https://images.unsplash.com/photo-1558788353-f76d92427f16?w=400"],
                "videos": ["https://example.com/max-video.mp4"],
                "personality": ["friendly", "energetic", "loyal"],
                "breederName": "Golden Dreams Kennel",
                "breederRating": 4.8,
                "price": 95000.00,
                "available": True
            },
            {
                "name": "Buddy",
                "species": "dogs",
                "breed": "Labrador Retriever",
                "age": 3,
                "weight": 35.0,
                "description": "Playful chocolate Labrador with excellent temperament. Great with children and other pets. Trained basic commands.",
                "images": ["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"],
                "videos": [],
                "personality": ["playful", "loyal", "intelligent"],
                "breederName": "Happy Paws",
                "breederRating": 4.7,
                "price": 85000.00,
                "available": True
            },
            {
                "name": "Rocky",
                "species": "dogs",
                "breed": "German Shepherd",
                "age": 1,
                "weight": 28.0,
                "description": "Strong and intelligent German Shepherd. Alert and protective family guardian. Excellent bloodline, trained for obedience.",
                "images": ["https://images.unsplash.com/photo-1568572933382-74d440641117?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"],
                "videos": [],
                "personality": ["intelligent", "protective", "loyal"],
                "breederName": "Shepherd Elite",
                "breederRating": 4.9,
                "price": 110000.00,
                "available": True
            },
            {
                "name": "Charlie",
                "species": "dogs",
                "breed": "Beagle",
                "age": 2,
                "weight": 12.0,
                "description": "Small but mighty Beagle with excellent hunting instincts. Friendly and curious personality. Great for apartment living.",
                "images": ["https://images.unsplash.com/photo-1505628346881-b72b27e84530?w=400"],
                "videos": [],
                "personality": ["friendly", "curious", "energetic"],
                "breederName": "Beagle House",
                "breederRating": 4.6,
                "price": 65000.00,
                "available": True
            },
            {
                "name": "Duke",
                "species": "dogs",
                "breed": "Rottweiler",
                "age": 4,
                "weight": 50.0,
                "description": "Magnificent Rottweiler with calm temperament. Despite reputation, very affectionate and family-oriented. Well-trained.",
                "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"],
                "videos": [],
                "personality": ["calm", "loyal", "protective"],
                "breederName": "Noble Rotts",
                "breederRating": 4.8,
                "price": 120000.00,
                "available": True
            },
            # CATS
            {
                "name": "Whiskers",
                "species": "cats",
                "breed": "Persian",
                "age": 1,
                "weight": 4.5,
                "description": "Elegant and refined Persian cat with luxurious long coat. Calm and affectionate. Requires regular grooming.",
                "images": ["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"],
                "videos": [],
                "personality": ["calm", "affectionate", "elegant"],
                "breederName": "Purrfect Cats",
                "breederRating": 4.9,
                "price": 55000.00,
                "available": True
            },
            {
                "name": "Luna",
                "species": "cats",
                "breed": "Siamese",
                "age": 2,
                "weight": 3.2,
                "description": "Beautiful Siamese with striking blue eyes. Vocal and interactive. Loves attention and playtime.",
                "images": ["https://images.unsplash.com/photo-1513360371669-4a8e1949883e?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"],
                "videos": [],
                "personality": ["vocal", "playful", "affectionate"],
                "breederName": "Siamese Dreams",
                "breederRating": 4.8,
                "price": 48000.00,
                "available": True
            },
            {
                "name": "Shadow",
                "species": "cats",
                "breed": "Black Domestic Shorthair",
                "age": 3,
                "weight": 4.0,
                "description": "Sleek black cat with golden eyes. Independent but loving. Perfect for quiet homes. Excellent mouser.",
                "images": ["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"],
                "videos": [],
                "personality": ["independent", "loving", "intelligent"],
                "breederName": "Shadow's Sanctuary",
                "breederRating": 4.7,
                "price": 35000.00,
                "available": True
            },
            {
                "name": "Mittens",
                "species": "cats",
                "breed": "British Shorthair",
                "age": 2,
                "weight": 5.5,
                "description": "Plump and cuddly British Shorthair with grey coat. Very calm and sociable. Great family pet.",
                "images": ["https://images.unsplash.com/photo-1567517381829-ba595fac2ec0?w=400"],
                "videos": [],
                "personality": ["calm", "sociable", "cuddly"],
                "breederName": "British Beauties",
                "breederRating": 4.9,
                "price": 52000.00,
                "available": True
            },
            {
                "name": "Tiger",
                "species": "cats",
                "breed": "Orange Tabby",
                "age": 1,
                "weight": 3.8,
                "description": "Energetic and playful orange tabby. Full of personality and mischief. Loves interactive toys.",
                "images": ["https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400"],
                "videos": [],
                "personality": ["playful", "energetic", "mischievous"],
                "breederName": "Tabby House",
                "breederRating": 4.6,
                "price": 40000.00,
                "available": True
            },
        ]
        
        # Comprehensive Products Data with Kenyan Shillings (KES)
        products_data = [
            # DOG FOOD
            {
                "name": "Premium Adult Dog Food",
                "description": "High-quality dry dog food with balanced nutrition. Rich in protein and essential vitamins. Suitable for all dog breeds.",
                "category": "food",
                "petType": "dogs",
                "brand": "PetPro",
                "price": 3500.00,
                "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"],
                "stock": 50,
                "filters": ["adult", "nutritious"]
            },
            {
                "name": "Grain-Free Puppy Food",
                "description": "Specially formulated for puppies. No grains, rich in DHA for brain development. Supports healthy growth.",
                "category": "food",
                "petType": "dogs",
                "brand": "NutriPaws",
                "price": 4200.00,
                "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"],
                "stock": 35,
                "filters": ["puppy", "grain-free"]
            },
            {
                "name": "Senior Dog Food",
                "description": "Low-calorie formula for senior dogs. Easy to digest with joint support ingredients.",
                "category": "food",
                "petType": "dogs",
                "brand": "GoldenYears",
                "price": 3800.00,
                "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"],
                "stock": 25,
                "filters": ["senior", "low-calorie"]
            },
            # CAT FOOD
            {
                "name": "Premium Cat Food - Salmon",
                "description": "Delicious salmon flavor cat food. Complete nutrition for adult cats. Promotes healthy coat.",
                "category": "food",
                "petType": "cats",
                "brand": "FelineFresh",
                "price": 2800.00,
                "images": ["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"],
                "stock": 40,
                "filters": ["salmon", "adult"]
            },
            {
                "name": "Kitten Growth Formula",
                "description": "Specially designed for kittens aged 2-12 months. High protein for development.",
                "category": "food",
                "petType": "cats",
                "brand": "KittyStart",
                "price": 3200.00,
                "images": ["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"],
                "stock": 30,
                "filters": ["kitten", "growth"]
            },
            # DOG TOYS
            {
                "name": "Interactive Dog Toy Set",
                "description": "Set of 5 interactive toys to keep dogs entertained. Includes balls, ropes, and chew toys.",
                "category": "toys",
                "petType": "dogs",
                "brand": "PlayPets",
                "price": 2200.00,
                "images": ["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"],
                "stock": 45,
                "filters": ["interactive", "durable"]
            },
            {
                "name": "Durable Rope Tug Toy",
                "description": "Strong rope toy for aggressive chewers. Great for multi-dog families. Machine washable.",
                "category": "toys",
                "petType": "dogs",
                "brand": "ChewMaster",
                "price": 1500.00,
                "images": ["https://images.unsplash.com/photo-1535241749838-299277b6305f?w=400"],
                "stock": 50,
                "filters": ["rope", "durable"]
            },
            {
                "name": "Dog Puzzle Feeder",
                "description": "Keep your dog mentally stimulated. Improves problem-solving skills during feeding time.",
                "category": "toys",
                "petType": "dogs",
                "brand": "BrainPlay",
                "price": 2800.00,
                "images": ["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"],
                "stock": 20,
                "filters": ["puzzle", "mental-stimulation"]
            },
            # CAT TOYS
            {
                "name": "Feather Wand Cat Toy",
                "description": "Interactive feather wand toy. Stimulates hunting instincts. Great for exercise.",
                "category": "toys",
                "petType": "cats",
                "brand": "CatPlay",
                "price": 800.00,
                "images": ["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"],
                "stock": 60,
                "filters": ["interactive", "feather"]
            },
            {
                "name": "Cat Laser Toy",
                "description": "Safe laser toy for cats. Promotes exercise and play. Includes auto-timer feature.",
                "category": "toys",
                "petType": "cats",
                "brand": "LaserFun",
                "price": 1200.00,
                "images": ["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"],
                "stock": 30,
                "filters": ["laser", "interactive"]
            },
            # HABITATS
            {
                "name": "Deluxe Cat Bed",
                "description": "Soft and comfortable cat bed. Machine washable cover. Cozy cave design.",
                "category": "habitats",
                "petType": "cats",
                "brand": "CatsLounge",
                "price": 4500.00,
                "images": ["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"],
                "stock": 25,
                "filters": ["comfortable", "cave"]
            },
            {
                "name": "Multi-Level Cat Tree",
                "description": "5-level cat tree with scratching posts. Provides climbing and resting areas. Sturdy construction.",
                "category": "habitats",
                "petType": "cats",
                "brand": "CatsLounge",
                "price": 12000.00,
                "images": ["https://images.unsplash.com/photo-1521568547814-0a0a0d8a2d3a?w=400"],
                "stock": 10,
                "filters": ["climbing", "scratching-posts"]
            },
            # ACCESSORIES
            {
                "name": "Premium Dog Collar with Leash",
                "description": "Adjustable leather collar with matching leash. Comfortable and durable. Multiple sizes.",
                "category": "accessories",
                "petType": "dogs",
                "brand": "SafeGuard",
                "price": 2500.00,
                "images": ["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"],
                "stock": 35,
                "filters": ["leather", "adjustable"]
            },
            {
                "name": "Cat Harness and Leash Set",
                "description": "Lightweight and safe harness for cats. Perfect for outdoor walks. Escape-proof design.",
                "category": "accessories",
                "petType": "cats",
                "brand": "SafeGuard",
                "price": 1800.00,
                "images": ["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"],
                "stock": 20,
                "filters": ["lightweight", "safe"]
            },
            # GROOMING
            {
                "name": "Professional Dog Grooming Kit",
                "description": "Complete grooming set including clippers, scissors, and brush. Suitable for all coat types.",
                "category": "grooming",
                "petType": "dogs",
                "brand": "GroomPro",
                "price": 5500.00,
                "images": ["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"],
                "stock": 15,
                "filters": ["professional", "complete"]
            },
            {
                "name": "Cat Grooming Brush",
                "description": "Gentle de-matting brush for cats. Reduces shedding. Comfortable grip handle.",
                "category": "grooming",
                "petType": "cats",
                "brand": "GroomPro",
                "price": 1500.00,
                "images": ["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"],
                "stock": 40,
                "filters": ["gentle", "de-matting"]
            },
        ]
        
        # Create pets
        created_pets = []
        for pet in pets_data:
            created_pet = await prisma_client.pet.create(data=pet)
            created_pets.append(created_pet)
        
        # Create products
        created_products = []
        for product in products_data:
            created_product = await prisma_client.product.create(data=product)
            created_products.append(created_product)
        
        # Create reviews for products
        if len(created_products) > 0:
            review_comments = [
                "Excellent quality! My dog loves this food. Great value for money in KES.",
                "Good product, my dogs have shinier coats now.",
                "Worth every shilling! Highly recommended.",
                "Perfect for my puppy. Growing well with this food.",
                "Best interactive toy ever. Keeps my dog busy for hours.",
                "My cat goes crazy for the salmon flavor!",
                "Great grooming kit. Easy to use!",
            ]
            
            for i, comment in enumerate(review_comments[:min(len(review_comments), len(created_products))]):
                await prisma_client.review.create(data={
                    "userId": f"user_{i+1}",
                    "productId": created_products[i % len(created_products)].id,
                    "rating": 5 if i % 2 == 0 else 4,
                    "comment": comment
                })
        
        # Create reviews for pets
        if len(created_pets) > 0:
            pet_reviews = [
                {"petIndex": 0, "comment": "Max is absolutely amazing! Perfect temperament and beautiful coat.", "rating": 5},
                {"petIndex": 0, "comment": "Worth every shilling. Great family pet!", "rating": 5},
                {"petIndex": 1, "comment": "Buddy is the sweetest. Great breeder!", "rating": 5},
                {"petIndex": 2, "comment": "Rocky is intelligent and loyal. Best decision!", "rating": 5},
                {"petIndex": 4, "comment": "Duke is calm and protective. Great addition to family.", "rating": 4},
                {"petIndex": 5, "comment": "Whiskers is so elegant and affectionate. Highly recommended!", "rating": 5},
                {"petIndex": 6, "comment": "Luna brings so much joy and energy to our home.", "rating": 5},
            ]
            
            for i, review_data in enumerate(pet_reviews):
                pet_idx = review_data["petIndex"]
                if pet_idx < len(created_pets):
                    await prisma_client.review.create(data={
                        "userId": f"user_{i+1}",
                        "petId": created_pets[pet_idx].id,
                        "rating": review_data["rating"],
                        "comment": review_data["comment"]
                    })
        
        return {
            "message": "✅ Database seeded successfully!",
            "pets": len(created_pets),
            "products": len(created_products),
            "currency": "Kenyan Shillings (KES)"
        }
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")
