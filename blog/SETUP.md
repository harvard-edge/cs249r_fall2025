# Blog Social Features Setup

## Disqus Comments Setup

1. **Create Disqus Account**: 
   - Go to https://disqus.com/admin/signup/
   - Sign up with your preferred method

2. **Add New Site**:
   - Click "Add Disqus to Site"
   - Website Name: "CS249r Harvard"
   - Category: "Tech"
   - Language: English

3. **Configure Shortname**:
   - Your shortname will be something like `cs249r-harvard`
   - Update `_config.yml` with the correct shortname:
   ```yaml
   disqus:
     shortname: "your-actual-shortname"  # Replace with real shortname
   ```

4. **Verify Setup**:
   - Comments will appear automatically on blog posts using the `post` layout
   - Test with a sample blog post

## Social Sharing Features

The blog now includes:
- ✅ Twitter sharing (mentions @VJReddi)
- ✅ LinkedIn sharing
- ✅ Hacker News submission
- ✅ Reddit submission
- ✅ Jekyll SEO plugin for rich previews
- ✅ Open Graph meta tags

## Blog Post Creation

Use the blog-writer agent via `/blog` command:
1. `/blog` → agent asks for date/week
2. Add thoughts throughout the week
3. `/blog` → "generate week X" → creates polished post
4. Posts use `post` layout automatically

## Cross-posting Options

Consider cross-posting to:
- **Medium**: Import from RSS or manual copy
- **Dev.to**: Has canonical URL support
- **LinkedIn**: Native article publishing