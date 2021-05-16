#!/usr/bin/env ruby

# Open README.md
readme = 'README.md'
content = File.read(readme)

# Remove everything before `## Plugins` and after `## Themes`
# Count all the `- [` at the beginning of lines
count = content
    .gsub(/^[.\s\S\r\n]*## Plugins/, '')
    .gsub!(/## Themes[.\s\S\r\n]*$/, '')
    .scan(/^-\s+\[/m).size

if count.to_i > 100
    print "#{count} plugins found, "

    # Update <!--plugin_count-->???<!--/plugin_count--> placeholders in readme and update file
    content.gsub!(/<!--plugin_count-->\d*?<!--\/plugin_count-->/, "<!--plugin_count-->#{count}<!--/plugin_count-->")
    File.open(readme, "w") {|file| file.puts content }
    puts "#{readme} updated."
    exit(true)
    
else
    puts "error (found #{count} plugins)"
    exit(false)
    
end
