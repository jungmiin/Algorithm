function revalidateIndex(deliveries, pickups, dIndex, pIndex) {
    let [ddIndex, ppIndex] = [dIndex, pIndex]
    while (ddIndex >= 0) {
        if (deliveries[ddIndex] > 0) break
        else ddIndex -= 1
    }
    while (ppIndex >= 0) {
        if (pickups[ppIndex] > 0) break
        else ppIndex -= 1
    }
    return [ddIndex, ppIndex]
}

function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let [dIndex, pIndex] = revalidateIndex(deliveries, pickups, n-1, n-1)
    let truck = 0;
    // console.log(deliveries+"\n"+pickups+"\n"+dIndex+" "+pIndex+" "+answer+"\n")
    while (dIndex >= 0 || pIndex >= 0) {
        [dIndex, pIndex] = revalidateIndex(deliveries, pickups, dIndex, pIndex)
        answer += (Math.max(dIndex, pIndex)+1)*2
        let ddIndex = dIndex;
        let ppIndex = pIndex
        while (truck < cap) {
            if (ddIndex < 0) break
            if (deliveries[ddIndex] > 0) {
                let delivery = deliveries[ddIndex]
                let remainDelivery = Math.max(0, delivery-(cap-truck))
                deliveries[ddIndex] = remainDelivery
                truck = Math.min(cap, truck+delivery)
                ddIndex = remainDelivery === 0 ? ddIndex-1 : ddIndex
            } else {
                ddIndex -= 1
            }
        }
        dIndex = ddIndex
        truck = 0
        while (truck < cap) {
            if (ppIndex < 0) break
            if (pickups[ppIndex] > 0) {
                let pickup = pickups[ppIndex]
                let remainPickup = Math.max(0, pickup-(cap-truck))
                pickups[ppIndex] = remainPickup
                truck = Math.min(cap, truck+pickup)
                ppIndex = remainPickup === 0 ? ppIndex - 1 : ppIndex
            } else {
                ppIndex -= 1
            }
        }
        pIndex = ppIndex
        truck = 0
        // console.log(deliveries+"\n"+pickups+"\n"+dIndex+" "+pIndex+" "+answer+"\n")
    }
    return answer
}