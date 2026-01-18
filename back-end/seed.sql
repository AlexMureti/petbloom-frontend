-- Clear existing data
TRUNCATE TABLE "Review" CASCADE;
TRUNCATE TABLE "Message" CASCADE;
TRUNCATE TABLE "UserAddress" CASCADE;
TRUNCATE TABLE "Product" CASCADE;
TRUNCATE TABLE "Pet" CASCADE;

-- Insert Pets (Dogs)
INSERT INTO "Pet" (name, species, breed, age, weight, description, images, videos, personality, "breederName", "breederRating", price, available) VALUES
('Max', 'dogs', 'Golden Retriever', 2, 30, 'Friendly and energetic golden retriever with beautiful cream coat. Perfect for active families. Fully vaccinated and dewormed.', '["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400", "https://images.unsplash.com/photo-1558788353-f76d92427f16?w=400"]', '["https://example.com/max-video.mp4"]', '["friendly", "energetic", "loyal"]', 'Golden Dreams Kennel', 4.8, 95000.00, true),
('Buddy', 'dogs', 'Labrador Retriever', 3, 35, 'Playful chocolate Labrador with excellent temperament. Great with children and other pets. Trained basic commands.', '["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"]', '[]', '["playful", "loyal", "intelligent"]', 'Happy Paws', 4.7, 85000.00, true),
('Rocky', 'dogs', 'German Shepherd', 1, 28, 'Strong and intelligent German Shepherd. Alert and protective family guardian. Excellent bloodline, trained for obedience.', '["https://images.unsplash.com/photo-1568572933382-74d440641117?w=400", "https://images.unsplash.com/photo-1552053831-71594a27c62d?w=400"]', '[]', '["intelligent", "protective", "loyal"]', 'Shepherd Elite', 4.9, 110000.00, true),
('Charlie', 'dogs', 'Beagle', 2, 12, 'Small but mighty Beagle with excellent hunting instincts. Friendly and curious personality. Great for apartment living.', '["https://images.unsplash.com/photo-1505628346881-b72b27e84530?w=400"]', '[]', '["friendly", "curious", "energetic"]', 'Beagle House', 4.6, 65000.00, true),
('Duke', 'dogs', 'Rottweiler', 4, 50, 'Magnificent Rottweiler with calm temperament. Despite reputation, very affectionate and family-oriented. Well-trained.', '["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"]', '[]', '["calm", "loyal", "protective"]', 'Noble Rotts', 4.8, 120000.00, true);

-- Insert Pets (Cats)
INSERT INTO "Pet" (name, species, breed, age, weight, description, images, videos, personality, "breederName", "breederRating", price, available) VALUES
('Whiskers', 'cats', 'Persian', 1, 4.5, 'Elegant and refined Persian cat with luxurious long coat. Calm and affectionate. Requires regular grooming.', '["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"]', '[]', '["calm", "affectionate", "elegant"]', 'Purrfect Cats', 4.9, 55000.00, true),
('Luna', 'cats', 'Siamese', 2, 3.2, 'Beautiful Siamese with striking blue eyes. Vocal and interactive. Loves attention and playtime.', '["https://images.unsplash.com/photo-1513360371669-4a8e1949883e?w=400", "https://images.unsplash.com/photo-1606214174585-fe31582dc1d7?w=400"]', '[]', '["vocal", "playful", "affectionate"]', 'Siamese Dreams', 4.8, 48000.00, true),
('Shadow', 'cats', 'Black Domestic Shorthair', 3, 4.0, 'Sleek black cat with golden eyes. Independent but loving. Perfect for quiet homes. Excellent mouser.', '["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"]', '[]', '["independent", "loving", "intelligent"]', 'Shadow''s Sanctuary', 4.7, 35000.00, true),
('Mittens', 'cats', 'British Shorthair', 2, 5.5, 'Plump and cuddly British Shorthair with grey coat. Very calm and sociable. Great family pet.', '["https://images.unsplash.com/photo-1567517381829-ba595fac2ec0?w=400"]', '[]', '["calm", "sociable", "cuddly"]', 'British Beauties', 4.9, 52000.00, true),
('Tiger', 'cats', 'Orange Tabby', 1, 3.8, 'Energetic and playful orange tabby. Full of personality and mischief. Loves interactive toys.', '["https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400"]', '[]', '["playful", "energetic", "mischievous"]', 'Tabby House', 4.6, 40000.00, true);

-- Insert Products (Food)
INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters) VALUES
('Premium Adult Dog Food', 'High-quality dry dog food with balanced nutrition. Rich in protein and essential vitamins. Suitable for all dog breeds.', 'food', 'dogs', 'PetPro', 3500.00, '["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"]', 50, '["adult", "nutritious"]'),
('Grain-Free Puppy Food', 'Specially formulated for puppies. No grains, rich in DHA for brain development. Supports healthy growth.', 'food', 'dogs', 'NutriPaws', 4200.00, '["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"]', 35, '["puppy", "grain-free"]'),
('Senior Dog Food', 'Low-calorie formula for senior dogs. Easy to digest with joint support ingredients.', 'food', 'dogs', 'GoldenYears', 3800.00, '["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"]', 25, '["senior", "low-calorie"]'),
('Premium Cat Food - Salmon', 'Delicious salmon flavor cat food. Complete nutrition for adult cats. Promotes healthy coat.', 'food', 'cats', 'FelineFresh', 2800.00, '["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"]', 40, '["salmon", "adult"]'),
('Kitten Growth Formula', 'Specially designed for kittens aged 2-12 months. High protein for development.', 'food', 'cats', 'KittyStart', 3200.00, '["https://images.unsplash.com/photo-1537462715957-923ec97dd6f0?w=400"]', 30, '["kitten", "growth"]');

-- Insert Products (Toys)
INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters) VALUES
('Interactive Dog Toy Set', 'Set of 5 interactive toys to keep dogs entertained. Includes balls, ropes, and chew toys.', 'toys', 'dogs', 'PlayPets', 2200.00, '["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"]', 45, '["interactive", "durable"]'),
('Durable Rope Tug Toy', 'Strong rope toy for aggressive chewers. Great for multi-dog families. Machine washable.', 'toys', 'dogs', 'ChewMaster', 1500.00, '["https://images.unsplash.com/photo-1535241749838-299277b6305f?w=400"]', 50, '["rope", "durable"]'),
('Dog Puzzle Feeder', 'Keep your dog mentally stimulated. Improves problem-solving skills during feeding time.', 'toys', 'dogs', 'BrainPlay', 2800.00, '["https://images.unsplash.com/photo-1570158108855-a920fb1b81d9?w=400"]', 20, '["puzzle", "mental-stimulation"]'),
('Feather Wand Cat Toy', 'Interactive feather wand toy. Stimulates hunting instincts. Great for exercise.', 'toys', 'cats', 'CatPlay', 800.00, '["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"]', 60, '["interactive", "feather"]'),
('Cat Laser Toy', 'Safe laser toy for cats. Promotes exercise and play. Includes auto-timer feature.', 'toys', 'cats', 'LaserFun', 1200.00, '["https://images.unsplash.com/photo-1559163499-64dd58e07650?w=400"]', 30, '["laser", "interactive"]');

-- Insert Products (Habitats)
INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters) VALUES
('Deluxe Cat Bed', 'Soft and comfortable cat bed. Machine washable cover. Cozy cave design.', 'habitats', 'cats', 'CatsLounge', 4500.00, '["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"]', 25, '["comfortable", "cave"]'),
('Multi-Level Cat Tree', '5-level cat tree with scratching posts. Provides climbing and resting areas. Sturdy construction.', 'habitats', 'cats', 'CatsLounge', 12000.00, '["https://images.unsplash.com/photo-1521568547814-0a0a0d8a2d3a?w=400"]', 10, '["climbing", "scratching-posts"]');

-- Insert Products (Accessories)
INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters) VALUES
('Premium Dog Collar with Leash', 'Adjustable leather collar with matching leash. Comfortable and durable. Multiple sizes.', 'accessories', 'dogs', 'SafeGuard', 2500.00, '["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"]', 35, '["leather", "adjustable"]'),
('Cat Harness and Leash Set', 'Lightweight and safe harness for cats. Perfect for outdoor walks. Escape-proof design.', 'accessories', 'cats', 'SafeGuard', 1800.00, '["https://images.unsplash.com/photo-1585110396000-c9ffd4d4b3f0?w=400"]', 20, '["lightweight", "safe"]');

-- Insert Products (Grooming)
INSERT INTO "Product" (name, description, category, "petType", brand, price, images, stock, filters) VALUES
('Professional Dog Grooming Kit', 'Complete grooming set including clippers, scissors, and brush. Suitable for all coat types.', 'grooming', 'dogs', 'GroomPro', 5500.00, '["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"]', 15, '["professional", "complete"]'),
('Cat Grooming Brush', 'Gentle de-matting brush for cats. Reduces shedding. Comfortable grip handle.', 'grooming', 'cats', 'GroomPro', 1500.00, '["https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400"]', 40, '["gentle", "de-matting"]');

-- Insert Reviews for Products
INSERT INTO "Review" ("userId", "productId", rating, comment, "createdAt") 
SELECT 'user_001', id, 5, 'Excellent quality! My dog loves this food. Great value for money in KES.', NOW() FROM "Product" WHERE name = 'Premium Adult Dog Food'
UNION ALL
SELECT 'user_002', id, 4, 'Good product, my dogs have shinier coats now.', NOW() FROM "Product" WHERE name = 'Premium Adult Dog Food'
UNION ALL
SELECT 'user_003', id, 5, 'Worth every shilling! Highly recommended.', NOW() FROM "Product" WHERE name = 'Premium Adult Dog Food'
UNION ALL
SELECT 'user_001', id, 5, 'Perfect for my puppy. Growing well with this food.', NOW() FROM "Product" WHERE name = 'Grain-Free Puppy Food'
UNION ALL
SELECT 'user_004', id, 4, 'Durable and my dog enjoys the variety of toys.', NOW() FROM "Product" WHERE name = 'Interactive Dog Toy Set'
UNION ALL
SELECT 'user_005', id, 5, 'My cat goes crazy for the salmon flavor!', NOW() FROM "Product" WHERE name = 'Premium Cat Food - Salmon'
UNION ALL
SELECT 'user_006', id, 5, 'Best interactive toy ever. Keeps my dog busy for hours.', NOW() FROM "Product" WHERE name = 'Interactive Dog Toy Set';

-- Insert Reviews for Pets
INSERT INTO "Review" ("userId", "petId", rating, comment, "createdAt")
SELECT 'user_001', id, 5, 'Max is absolutely amazing! Perfect temperament and beautiful coat.', NOW() FROM "Pet" WHERE name = 'Max'
UNION ALL
SELECT 'user_002', id, 5, 'Worth every shilling. Great family pet!', NOW() FROM "Pet" WHERE name = 'Max'
UNION ALL
SELECT 'user_003', id, 5, 'Buddy is the sweetest. Great breeder!', NOW() FROM "Pet" WHERE name = 'Buddy'
UNION ALL
SELECT 'user_004', id, 5, 'Rocky is intelligent and loyal. Best decision!', NOW() FROM "Pet" WHERE name = 'Rocky'
UNION ALL
SELECT 'user_005', id, 4, 'Duke is calm and protective. Great addition to family.', NOW() FROM "Pet" WHERE name = 'Duke';

-- Insert User Addresses
INSERT INTO "UserAddress" ("userId", street, city, state, "zipCode", country, "isDefault") VALUES
('user_001', '123 Kenyatta Avenue', 'Nairobi', 'Nairobi County', '00100', 'Kenya', true),
('user_001', '456 Moi Road', 'Mombasa', 'Coast County', '80100', 'Kenya', false),
('user_002', '789 Ahmed Gaddafi Lane', 'Nairobi', 'Nairobi County', '00600', 'Kenya', true),
('user_003', '321 Ring Road', 'Kisumu', 'Kisumu County', '40100', 'Kenya', true);

-- Insert Messages
INSERT INTO "Message" ("senderId", "recipientId", content, read, "createdAt") VALUES
('user_002', 'user_001', 'Hi! I''m very interested in Max the Golden Retriever. Is he still available? When can we arrange a viewing?', false, NOW()),
('user_001', 'user_002', 'Yes, Max is available! We can arrange a viewing this weekend. What time works best for you?', false, NOW()),
('user_003', 'user_001', 'Interested in Rocky the German Shepherd. What is the current price in KES?', false, NOW()),
('user_001', 'user_003', 'Rocky is priced at KES 110,000. He''s a wonderful dog with excellent bloodline!', false, NOW()),
('user_004', 'user_001', 'Do you have any Siamese cats available? Particularly interested in Luna.', false, NOW()),
('user_001', 'user_004', 'Yes! Luna is available at KES 48,000. She''s very interactive and loving!', false, NOW());
