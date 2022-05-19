string manachers_algorithm(string &s) {
    if (s.empty()) {
        return "";
    }
    string t = "^#";

    for (auto c : s) {
        t.push_back(c);
        t.push_back('#');
    }
    t.push_back('$');
        
    vector<int> radii(t.size());
    int c = 1, d = 1;
    
    for(int i = 2; i < radii.size()-1; ++i) {
        int mirror = c-(i-c);
        radii[i] = max(0, min(radii[mirror], d-i));
        while(t[i-radii[i]-1] == t[i+radii[i]+1]) {
            radii[i]++;
        }
        if (radii[i] + i > d) {
            c = i;
            d = i + radii[i];
        }
    }
    
    int center = 1, max_rad = radii[1];
    for (int i = 1; i < radii.size()-1; ++i) {
        if (radii[i] > max_rad) {
            center = i;
            max_rad = radii[i];
        }
    }
    
    int start = (center - max_rad) / 2;
    int end = (center + max_rad) / 2;
    
    return s.substr(start, end-start);
    
}