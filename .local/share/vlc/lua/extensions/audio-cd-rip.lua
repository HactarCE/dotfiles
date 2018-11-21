profiles={
	{"Audio CD -> mp3", " :cdda-track=? :sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:file{mux=mp3,dst=\"H:\\Track ?.mp3\"}"},
	{"Audio CD -> wav", " :cdda-track=? :sout=#transcode{vcodec=none,acodec=s16l,ab=128,channels=2,samplerate=44100}:file{mux=wav,dst=\"H:\\Track ?.wav\"}"},
}

-----

function descriptor()
	return {
		title = "Audio CD ripping helper",
		capabilities={},
	}
end

function activate()
	create_dialog()
end

function deactivate()
end

function meta_changed()
end

function close()
    vlc.deactivate()
end

-----

function create_dialog()
	d = vlc.dialog(descriptor().title)
	d:add_label(string.rep("&nbsp;",50),1,1,1,1)
	d:add_label(string.rep("&nbsp;",50),2,1,1,1)
	d:add_label(string.rep("&nbsp;",50),3,1,1,1)
	d:add_label(string.rep("&nbsp;",50),4,1,1,1)
	d:add_label(string.rep("&nbsp;",50),5,1,1,1)
	----
	d:add_label("Source MRL: ",1,1,1,1)
	ti_mrl = d:add_text_input("cdda:///E:/",2,1,1,1)
	d:add_label("(Media > Open Disc... > Audio CD)",3,1,2,1)

	d:add_label("Tracks: ",1,2,1,1)
	ti_tracks = d:add_text_input("15",2,2,1,1)
	d:add_label("Then ? in output string represents the counter.",3,2,2,1)

	d:add_label("Output options: \\ Profiles:",1,3,1,1)
	dd_profile = d:add_dropdown(2,3,1,1)
	for i,v in ipairs(profiles) do
		dd_profile:add_value(v[1],i)
	end
	d:add_button("Apply profile", click_Profile, 3,3,1,1)
	d:add_label("(Media > Stream... wizard)",4,3,1,1)

	ti_sout_string = d:add_text_input(profiles[1][2], 1,4,5,1)

	d:add_button("Enqueue converting tracks", click_Convert, 2,5,1,1)
	d:add_label("Then start the 1st converting track in playlist (View > Playlist).",3,5,2,1)
end

function click_Profile()
	ti_sout_string:set_text(profiles[dd_profile:get_value()][2])
end

function click_Convert()
	local j=tonumber(ti_tracks:get_text())
	if not j then j=1 ti_tracks:set_text(j) end
	local source_string = ti_mrl:get_text()
	local options_string = ti_sout_string:get_text()
	local table_items={}
	table.insert(table_items,{path="vlc://pause:5", name="[Convert! START]", options={}})
	for i=1,j do
		table.insert(table_items,{path=source_string, name="[Convert!] Audio CD - Track "..i, options=SplitString(string.gsub(options_string,"%?",i), " :")})
	end
	table.insert(table_items,{path="vlc://pause:10", name="[Convert! END]", options={}})
	vlc.playlist.enqueue(table_items)
end

-----

function SplitString(s, d) -- string, delimiter pattern
	local t={}
	local i=1
	local ss, j, k
	local b=false
	while true do
		j,k = string.find(s,d,i)
		if j then
			ss=string.sub(s,i,j-1)
			i=k+1
		else
			ss=string.sub(s,i)
			b=true
		end
		table.insert(t, ss)
		if b then break end
	end
	return t
end
