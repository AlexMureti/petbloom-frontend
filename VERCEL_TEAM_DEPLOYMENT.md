# PetBloom Vercel Team Deployment Plan

## Team Configuration
- **Team ID**: `team_G7pAfOmi7diMewBtcWrdXuNx`
- **Project**: petbloom-frontend
- **Framework**: Vite (React)

## Current Project Status

### ✅ Already Configured
1. `vercel.json` - Proper Vercel configuration with:
   - Build command: `npm run build`
   - Output directory: `dist`
   - Environment variables for API and Firebase
   - Rewrite rules for SPA routing

2. Package.json - Standard Vite build setup

### ⚠️ Items to Complete
1. Install Vercel CLI
2. Login to Vercel with team context
3. Deploy with team configuration

## Deployment Steps

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login and Link to Team
```bash
vercel login
# After login, link project to team:
vercel link --team=G7pAfOmi7diMewBtcWrdXuNx
```

### Step 3: Deploy to Vercel (Production)
```bash
vercel --prod --team=G7pAfOmi7diMewBtcWrdXuNx
```

### Alternative: Using Vercel Dashboard with Team
1. Go to https://vercel.com/teams/G7pAfOmi7diMewBtcWrdXuNx
2. Click "Add New Project"
3. Import from GitHub: `AlexMureti/petbloom-frontend`
4. Configure settings (already pre-configured in vercel.json)
5. Deploy

## Environment Variables Required
The following environment variables are already configured in `vercel.json`:

```
VITE_API_URL=https://petbloom-frontend-production.up.railway.app/api/v1
VITE_FIREBASE_API_KEY=AIzaSyD8hxlXo7mjuM1e7Yg_DCCRLrIyrhW7TRA
VITE_FIREBASE_AUTH_DOMAIN=petbloom-71bbc.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=petbloom-71bbc
VITE_FIREBASE_STORAGE_BUCKET=petbloom-71bbc.firebasestorage.app
VITE_FIREBASE_MESSAGING_SENDER_ID=918044598228
VITE_FIREBASE_APP_ID=1:918044598228:web:5a85cb15270f08fed64041
VITE_FIREBASE_MEASUREMENT_ID=G-2311X47GF1
```

## Verification Checklist
- [ ] Vercel CLI installed
- [ ] Logged in with team context
- [ ] Project linked to team: `team_G7pAfOmi7diMewBtcWrdXuNx`
- [ ] Deployment successful
- [ ] Visit deployed URL and verify it loads
- [ ] Test API connectivity
- [ ] Check browser console for errors

## Quick Deploy Command (after setup)
```bash
vercel --prod --team=G7pAfOmi7diMewBtcWrdXuNx
```

## Expected Output
Once deployed, your site will be available at:
- Production: `https://petbloom-frontend-<hash>.vercel.app`
- Or custom domain if configured

