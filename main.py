import server
import output

if __name__ == '__main__':
    
    num_locations = int(input())
    locations = []
    for i in range(num_locations):
        locations.append(input())
    num_outputs = int(input())
    outputs = []
    for i in range(num_outputs):
        outputs.append(input())

    url = server.build_search_url(locations[0], locations[1:])
    D1 = server.get_result(url)
    url2 = server.build_elevation_url(D1)
    print("HEREEEE", url2)
    D2 = server.get_result(url2)
    result = server.refine(D1, D2)

    output_objects = []
    for i in outputs:
        
        output_objects.append(eval('output.' + i + '()'))
    for i in output_objects:
        print(i.output(result) + '\n')
            
        
