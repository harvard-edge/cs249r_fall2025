source "https://rubygems.org"

# Local dev: use Jekyll directly instead of github-pages
gem "jekyll", "~> 3.9.5"
gem "webrick", "~> 1.8"
gem "csv"
gem "logger"
gem "base64"
gem "bigdecimal"

# gem "jekyll-feed"  # Commented out temporarily due to eventmachine build issues
gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll-include-cache"
gem "kramdown-parser-gfm"

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
