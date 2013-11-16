<?php
$app->get( '/meal', function () {
    include '../show_active_meals.php';
    $return = array();
    foreach( $meals as $meal ) {
        $entry = new stdclass();
        $entry->id          = $meal->getId();
        $entry->photo       = 'http://fostercityvillage.org/wp-content/uploads/2012/10/meal-m.jpg';
        $entry->description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel facilisis ligula. Fusce commodo lorem consectetur tortor gravida semper. Aliquam id nunc eros. Suspendisse eu quam at nibh pulvinar mollis. Phasellus consequat nisl sit amet hendrerit feugiat. Vestibulum aliquam, nulla consequat condimentum placerat, erat dui molestie dolor, sit amet pharetra est mi in purus. In sit amet tempus erat, ut luctus ante.';
        $entry->coins       = '2';
        $return[] = $entry;
    }

    echo json_encode( $return );
});
