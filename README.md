# 🚀 SpeedCheck - Premium Internet Speed Test

A production-ready, high-performance internet speed test application similar to Fast.com. Built with FastAPI backend and vanilla JavaScript frontend.

## ✨ Features

- **Real-time Speed Measurement**: Live Mbps counting during tests
- **Parallel Download Streams**: 3+ simultaneous connections for accurate speed testing
- **Upload Speed Testing**: Measures upload performance with real data
- **Latency Measurement**: Accurate ping/latency calculation with averaging
- **Premium UI**: VIP-level design with glassmorphism effects and smooth animations
- **Dark Theme**: Modern, eye-friendly dark interface
- **Fully Responsive**: Optimized for mobile and desktop
- **Serverless Compatible**: Ready for Vercel deployment
- **High Performance**: Async streaming with optimized I/O

## 📁 Project Structure

```
wifi-speed-test/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── routers/
│   │       ├── __init__.py
│   │       └── speed_test.py
│   ├── api/
│   │   └── speed.py          # Vercel serverless function
│   ├── requirements.txt       # Python dependencies
│   └── vercel.json           # Vercel configuration
├── public/
│   ├── index.html            # Frontend HTML
│   ├── styles.css            # Modern responsive styling
│   └── script.js             # Speed test logic
└── README.md                 # This file
```

## 🚀 Getting Started

### Local Development

#### Prerequisites
- Python 3.8+
- pip (Python package manager)

#### Installation & Running

1. **Clone the repository**
```bash
git clone https://github.com/sadxd8/wifi-speed-test.git
cd wifi-speed-test
```

2. **Install backend dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Run the FastAPI server**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. **Open the frontend**
- Navigate to `public/index.html` in your browser
- Or serve it with a simple HTTP server:
```bash
cd ../public
python -m http.server 8080
```
- Visit `http://localhost:8080`

### API Endpoints

#### GET /download
- **Description**: Serves 50MB of random data for download speed testing
- **Response**: Binary stream (50MB)
- **Use**: For measuring download speed

#### POST /upload
- **Description**: Accepts binary file upload
- **Request**: Multipart form data with file
- **Response**: `{"uploaded": bytes_count}`
- **Use**: For measuring upload speed

#### GET /ping
- **Description**: Quick latency measurement endpoint
- **Response**: `{"timestamp": unix_timestamp}`
- **Use**: For measuring latency/ping

## 📱 Frontend Features

### Speed Test Process

1. **Ping Test**: Measures latency with 4 averaged requests (~1-2s)
2. **Download Test**: 3 parallel streams downloading 50MB combined (~10s)
3. **Upload Test**: Uploads 25MB of random data (~8-10s)

### UI Components

- **Speed Circle**: Live animated display of current speed
- **Status Indicator**: Real-time test status and loading animation
- **Progress Bar**: Visual test progress indicator
- **Results Grid**: Final results showing Download/Upload/Latency
- **Auto-start Checkbox**: Repeat tests automatically

### Browser Support

- Chrome/Edge 88+
- Firefox 85+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🌐 Deployment on Vercel

### Prerequisites
- Vercel account (https://vercel.com)
- GitHub repository connected to Vercel

### Deployment Steps

1. **Push to GitHub**
```bash
git add .
git commit -m "Deploy SpeedCheck"
git push origin main
```

2. **Connect to Vercel**
- Go to https://vercel.com/dashboard
- Click "Add New..." → "Project"
- Select your GitHub repository
- Click "Import"

3. **Configure Project**
- **Framework**: Detect framework automatically or select "Other"
- **Root Directory**: Leave as default
- **Environment Variables**: Not required for basic setup

4. **Deploy**
- Click "Deploy"
- Vercel will automatically build and deploy your application
- Your app will be live at `https://your-project.vercel.app`

### Environment Variables (Optional)

No environment variables are required for basic deployment. For production, you may want to add:

- `API_BASE_URL`: Override API base URL in frontend
- `CORS_ORIGINS`: Comma-separated list of allowed CORS origins

### Vercel Configuration

The `backend/vercel.json` file is pre-configured for:
- Python framework detection
- FastAPI application setup
- Serverless function memory (3008MB)
- Maximum execution time (60 seconds)
- Route mapping for API and static files

## ⚡ Performance Optimization

### Backend Optimizations
- **Async Generators**: Efficient streaming of large files
- **Chunked Transfer**: 1MB chunks for optimal memory usage
- **Parallel Requests**: Supports concurrent uploads/downloads
- **CORS Enabled**: No cross-origin restrictions

### Frontend Optimizations
- **Vanilla JavaScript**: No framework overhead
- **Efficient DOM Updates**: Minimal reflows/repaints
- **Real-time Calculations**: Live speed updates during tests
- **CSS Animations**: GPU-accelerated smooth transitions
- **Responsive Design**: Mobile-first approach

## 🔧 Configuration

### Changing Download Test Size
Edit `backend/app/routers/speed_test.py`:
```python
DOWNLOAD_SIZE = 52428800  # Change this value (in bytes)
```

### Changing Upload Test Size
Edit `public/script.js` in `measureUploadSpeed()`:
```javascript
const uploadSize = 25 * 1024 * 1024;  // Change this value (in bytes)
```

### Changing Test Duration
Edit `public/script.js` in `measureDownloadSpeed()`:
```javascript
10000  // Change timeout (in milliseconds)
```

## 🎨 UI Customization

### Colors
Edit CSS variables in `public/styles.css`:
```css
:root {
    --primary: #00d4ff;        /* Primary accent color */
    --accent: #ff006e;         /* Secondary accent color */
    --bg-dark: #0a0e27;        /* Dark background */
    --text-primary: #ffffff;   /* Primary text color */
    /* ... more variables ... */
}
```

### Fonts
Change font in `public/styles.css`:
```css
body {
    font-family: 'Your-Font', sans-serif;
}
```

## 📊 Test Accuracy

- **Ping**: Average of 4 measurements for accuracy
- **Download**: 3 parallel streams minimize variance
- **Upload**: Single 25MB stream for consistency
- **Result**: Real measurements, no artificial data

## 🐛 Troubleshooting

### API Connection Issues
- Ensure backend is running on `localhost:8000`
- Check browser console for CORS errors
- Verify API base URL in `public/script.js`

### Tests Not Starting
- Clear browser cache
- Try in incognito/private mode
- Check network tab for failed requests

### Slow Speeds Recorded
- Close other applications using bandwidth
- Move closer to WiFi router
- Run test during off-peak hours

## 📝 License

MIT License - Feel free to use for personal or commercial projects

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📧 Support

For issues, questions, or feedback:
- Open an issue on GitHub
- Check existing documentation
- Review the code comments

---

**Made with ❤️ for the open-source community**